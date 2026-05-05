"""
Testes minimos de integridade do corpus Alexandria v3.1.

Valida que a entry-exemplo (Python) contem todos os 14 blocos obrigatorios
e que o JSON Schema formal carrega corretamente.
"""

from pathlib import Path
import json
import yaml


CORPUS_ROOT = Path(__file__).resolve().parent.parent / "corpus"
ENTRY_PATH = CORPUS_ROOT / "entries" / "python.yaml"
SCHEMA_PATH = CORPUS_ROOT / "schema" / "alexandria-v3.1.json"


def _load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


class TestPythonEntry:
    """Verifica a integridade da entry Python contra o schema Alexandria."""

    def test_entry_file_exists(self):
        assert ENTRY_PATH.exists(), f"Arquivo de entry ausente: {ENTRY_PATH}"

    def test_python_entry_has_all_blocos(self):
        entry = _load_yaml(ENTRY_PATH)
        for i in range(1, 15):
            bloco_key = f"bloco_{i}"
            assert bloco_key in entry, (
                f"{bloco_key} ausente nos blocos de nivel superior da entry"
            )

    def test_meta_present(self):
        entry = _load_yaml(ENTRY_PATH)
        assert "meta" in entry, "Secao 'meta' ausente"
        assert "versao_schema" in entry["meta"], "meta.versao_schema ausente"
        assert entry["meta"]["versao_schema"] == "3.1"

    def test_bloco_1_nome_present(self):
        entry = _load_yaml(ENTRY_PATH)
        bloco = entry.get("bloco_1_metadados", {})
        assert "nome" in bloco, "bloco_1.nome ausente"
        assert bloco["nome"] == "Python"

    def test_bloco_4_metafora_present(self):
        entry = _load_yaml(ENTRY_PATH)
        bloco = entry.get("bloco_4_metafora_fundante", {})
        assert "definicao" in bloco, "bloco_4.definicao ausente"
        assert "modo_analogia_tats" in bloco, "bloco_4.modo_analogia_tats ausente"

    def test_bloco_6_savigny_4_dimensoes(self):
        entry = _load_yaml(ENTRY_PATH)
        bloco = entry.get("bloco_6_analise_savigny", {})
        dimensoes = ["gramatical", "semantica", "historica", "sistemica"]
        for dim in dimensoes:
            assert dim in bloco, f"bloco_6.{dim} ausente"

    def test_bloco_5_gilp_5_camadas(self):
        entry = _load_yaml(ENTRY_PATH)
        bloco = entry.get("bloco_5_interface_grammar", {})
        camadas = [
            "camada_1_cognitiva",
            "camada_2_infraestrutural",
            "camada_3_sistemica",
            "camada_4_ecossistemica",
            "camada_5_cultural",
        ]
        for cam in camadas:
            assert cam in bloco, f"bloco_5.{cam} ausente"

    def test_bloco_13_confianca(self):
        entry = _load_yaml(ENTRY_PATH)
        bloco = entry.get("bloco_13_acesso", {})
        assert "nivel_confianca" in bloco, "bloco_13.nivel_confianca ausente"
        assert bloco["nivel_confianca"] == "Medio"


class TestAlexandriaSchema:
    """Verifica a integridade do JSON Schema Alexandria v3.1."""

    def test_schema_file_exists(self):
        assert SCHEMA_PATH.exists(), f"Schema ausente: {SCHEMA_PATH}"

    def test_schema_loads(self):
        schema = _load_json(SCHEMA_PATH)
        assert "properties" in schema, "Schema sem campo 'properties'"
        assert "required" in schema, "Schema sem campo 'required'"
        assert len(schema["required"]) >= 10

    def test_schema_has_bloco_1(self):
        schema = _load_json(SCHEMA_PATH)
        props = schema.get("properties", {})
        assert any("bloco_1" in k for k in props), "Schema sem bloco_1"

    def test_schema_has_bloco_14(self):
        schema = _load_json(SCHEMA_PATH)
        props = schema.get("properties", {})
        assert any("bloco_14" in k for k in props), "Schema sem bloco_14"
