#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alexandria Corpus Validator - POC/MVP
Valida entries do corpus contra o Schema Alexandria v3.1

Uso: python scripts/validate_corpus.py
"""

import json
import sys
import os
from pathlib import Path

try:
    import yaml
    import jsonschema
except ImportError:
    print("Instale as dependencias primeiro:")
    print("  pip install jsonschema pyyaml")
    sys.exit(1)

CORPUS_DIR = Path(__file__).parent.parent / "corpus"
SCHEMA_PATH = CORPUS_DIR / "schema" / "alexandria-v3.1.json"
ENTRIES_DIR = CORPUS_DIR / "entries"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_entry(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_entry(entry, schema):
    jsonschema.validate(instance=entry, schema=schema)


def get_entry_stats(entry):
    stats = {}
    meta = entry.get("meta", {})
    stats["versao_schema"] = meta.get("versao_schema", "desconhecida")
    stats["slug"] = entry.get("bloco_1_metadados", {}).get("slug", "desconhecido")
    stats["nome"] = entry.get("bloco_1_metadados", {}).get("nome", "desconhecido")

    b2 = entry.get("bloco_2_classificacao_procp", {})
    stats["paradigmas"] = b2.get("eixo_2_paradigma", [])
    stats["era"] = b2.get("era_historica", "desconhecida")
    stats["distancia_silicio"] = b2.get("eixo_7_distancia_silicio", "?")

    b4 = entry.get("bloco_4_metafora_fundante", {})
    stats["metafora_fundante"] = b4.get("definicao", "N/A")
    stats["modo_analogia_tats"] = b4.get("modo_analogia_tats", "N/A")

    b13 = entry.get("bloco_13_acesso", {})
    stats["nivel_confianca"] = b13.get("nivel_confianca", "N/A")

    blocos_presentes = [
        key for key in entry.keys() if key.startswith("bloco_")
    ]
    stats["blocos_preenchidos"] = len(blocos_presentes)
    stats["total_blocos"] = 14

    return stats


def main():
    print("=" * 60)
    print("  Alexandria Corpus Validator v1.0")
    print("  Schema Alexandria v3.1 - POC/MVP")
    print("=" * 60)

    if not SCHEMA_PATH.exists():
        print(f"\nERRO: Schema nao encontrado em {SCHEMA_PATH}")
        sys.exit(1)

    if not ENTRIES_DIR.exists():
        print(f"\nERRO: Diretorio de entries nao encontrado em {ENTRIES_DIR}")
        sys.exit(1)

    schema = load_schema()
    print(f"\nSchema carregado: alexandria-v3.1.json")
    print(f"Propriedades definidas: {len(schema.get('properties', {}))}")
    print(f"Propriedades obrigatorias: {len(schema.get('required', []))}")

    yaml_files = sorted(ENTRIES_DIR.glob("*.yaml"))
    yml_files = sorted(ENTRIES_DIR.glob("*.yml"))
    all_entries = yaml_files + yml_files

    print(f"\nEntries encontradas: {len(all_entries)}")
    print("-" * 60)

    valid_count = 0
    error_count = 0

    for entry_path in all_entries:
        entry_name = entry_path.name
        print(f"\nValidando: {entry_name}")

        try:
            entry = load_entry(entry_path)
            validate_entry(entry, schema)
            stats = get_entry_stats(entry)
            print(f"  [OK] Validacao passou")
            print(f"       Linguagem: {stats['nome']} ({stats['slug']})")
            print(f"       Schema:    v{stats['versao_schema']}")
            print(f"       Paradigmas: {', '.join(stats['paradigmas'])}")
            print(f"       Era:        {stats['era']}")
            print(f"       Distancia:  {stats['distancia_silicio']}/10 do silicio")
            print(f"       Metafora:   {stats['metafora_fundante']}")
            print(f"       TATS:       {stats['modo_analogia_tats']}")
            print(f"       Confianca:  {stats['nivel_confianca']}")
            print(f"       Blocos:     {stats['blocos_preenchidos']}/{stats['total_blocos']}")
            valid_count += 1
        except jsonschema.ValidationError as e:
            print(f"  [ERRO] Validacao falhou")
            print(f"       Campo: {list(e.path) if e.path else 'raiz'}")
            print(f"       Mensagem: {e.message}")
            error_count += 1
        except Exception as e:
            print(f"  [ERRO] {type(e).__name__}: {e}")
            error_count += 1

    print("\n" + "=" * 60)
    print(f"  Resultado: {valid_count} validas, {error_count} com erro")
    print(f"  Total: {len(all_entries)} entries processadas")
    print("=" * 60)

    if error_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
