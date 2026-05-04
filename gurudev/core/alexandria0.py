"""
Biblioteca de Interoperabilidade Gurudev
Programação Comparada - Sistema de Ponte Universal entre Linguagens
"""

import json
import ast
import inspect
from typing import Dict, Any, List, Optional, Union, Callable
from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod

class ParadigmType(Enum):
    IMPERATIVE = "imperative"
    FUNCTIONAL = "functional"
    OBJECT_ORIENTED = "object_oriented"
    DECLARATIVE = "declarative"

class TypeSystem(Enum):
    DYNAMIC = "dynamic"
    STATIC = "static"
    GRADUAL = "gradual"

@dataclass
class LanguageProfile:
    name: str
    paradigms: List[ParadigmType]
    type_system: TypeSystem
    gurudev_compatibility: int
    interop_bridges: Dict[str, Any]

class ComparativeProgrammingDB:
    """Base de dados para análise comparativa de linguagens"""
    
    def __init__(self, db_path: str = "comparative_programming.json"):
        self.db_path = db_path
        self.data = self.load_database()
        self.profiles = self._build_profiles()
    
    def load_database(self) -> Dict[str, Any]:
        """Carrega base de dados JSON"""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._create_default_database()
    
    def _create_default_database(self) -> Dict[str, Any]:
        """Cria base de dados padrão se não existir"""
        return {
            "languages": {},
            "paradigms": {},
            "comparative_metrics": {},
            "interoperability_matrix": {}
        }
    
    def _build_profiles(self) -> Dict[str, LanguageProfile]:
        """Constrói perfis de linguagens a partir da base de dados"""
        profiles = {}
        
        for lang_name, lang_data in self.data.get("languages", {}).items():
            paradigms = [ParadigmType(p) for p in lang_data.get("paradigms", [])]
            
            type_sys = lang_data.get("typing", {}).get("system", "dynamic")
            type_system = TypeSystem(type_sys)
            
            compatibility = lang_data.get("interoperability", {}).get("gurudev_compatibility", 0)
            bridges = lang_data.get("interoperability", {})
            
            profiles[lang_name] = LanguageProfile(
                name=lang_name,
                paradigms=paradigms,
                type_system=type_system,
                gurudev_compatibility=compatibility,
                interop_bridges=bridges
            )
        
        return profiles
    
    def compare_languages(self, lang1: str, lang2: str) -> Dict[str, Any]:
        """Compara duas linguagens seguindo princípios da programação comparada"""
        
        if lang1 not in self.profiles or lang2 not in self.profiles:
            raise ValueError(f"Linguagem não encontrada na base de dados")
        
        profile1 = self.profiles[lang1]
        profile2 = self.profiles[lang2]
        
        # Análise paradigmática
        common_paradigms = set(profile1.paradigms) & set(profile2.paradigms)
        unique_paradigms = set(profile1.paradigms) ^ set(profile2.paradigms)
        
        # Análise de compatibilidade
        compatibility_diff = abs(profile1.gurudev_compatibility - profile2.gurudev_compatibility)
        
        # Análise de interoperabilidade
        interop_score = self._calculate_interop_score(profile1, profile2)
        
        return {
            "languages": [lang1, lang2],
            "paradigmatic_analysis": {
                "common_paradigms": [p.value for p in common_paradigms],
                "unique_paradigms": [p.value for p in unique_paradigms],
                "paradigmatic_distance": len(unique_paradigms)
            },
            "type_system_compatibility": profile1.type_system == profile2.type_system,
            "gurudev_compatibility_diff": compatibility_diff,
            "interoperability_score": interop_score,
            "recommended_bridge": self._recommend_bridge(profile1, profile2)
        }
    
    def _calculate_interop_score(self, profile1: LanguageProfile, profile2: LanguageProfile) -> float:
        """Calcula score de interoperabilidade entre duas linguagens"""
        base_score = (profile1.gurudev_compatibility + profile2.gurudev_compatibility) / 2
        
        # Bonus por paradigmas comuns
        common_paradigms = len(set(profile1.paradigms) & set(profile2.paradigms))
        paradigm_bonus = common_paradigms * 5
        
        # Bonus por compatibilidade de tipos
        type_bonus = 10 if profile1.type_system == profile2.type_system else 0
        
        return min(100, base_score + paradigm_bonus + type_bonus)
    
    def _recommend_bridge(self, profile1: LanguageProfile, profile2: LanguageProfile) -> str:
        """Recomenda ponte de interoperabilidade"""
        lang1_name = profile1.name
        lang2_name = profile2.name
        
        # Verifica se existe ponte nativa
        interop_matrix = self.data.get("interoperability_matrix", {})
        native_bridges = interop_matrix.get("native_bridges", {})
        
        bridge_key = f"{lang1_name}_{lang2_name}"
        reverse_bridge_key = f"{lang2_name}_{lang1_name}"
        
        if bridge_key in native_bridges:
            return f"Native bridge: {native_bridges[bridge_key]}"
        elif reverse_bridge_key in native_bridges:
            return f"Native bridge: {native_bridges[reverse_bridge_key]}"
        else:
            return "Universal Gurudev bridge recommended"

class GurudevInteropBridge(ABC):
    """Interface abstrata para pontes de interoperabilidade"""
    
    @abstractmethod
    def translate_syntax(self, code: str, source_lang: str, target_lang: str) -> str:
        pass
    
    @abstractmethod
    def map_types(self, type_info: Dict[str, Any], source_lang: str, target_lang: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def handle_paradigm_mismatch(self, paradigm_diff: List[str]) -> Dict[str, Any]:
        pass

class UniversalGurudevBridge(GurudevInteropBridge):
    """Ponte universal baseada no dodecálogo Gurudev"""
    
    def __init__(self, comp_db: ComparativeProgrammingDB):
        self.comp_db = comp_db
        self.dodecalogo = comp_db.data.get("dodecalogo_principles", {})
    
    def translate_syntax(self, code: str, source_lang: str, target_lang: str) -> str:
        """Traduz sintaxe entre linguagens usando AST universal"""
        # Implementação simplificada - na prática seria muito mais complexa
        
        if source_lang == "python" and target_lang == "javascript":
            # Exemplo básico de tradução Python -> JavaScript
            translations = {
                "def ": "function ",
                "True": "true",
                "False": "false",
                "None": "null",
                "print(": "console.log(",
                "    ": "  "  # Indentação Python para JavaScript
            }
            
            translated = code
            for py_syntax, js_syntax in translations.items():
                translated = translated.replace(py_syntax, js_syntax)
            
            return translated
        
        return f"// Tradução {source_lang} -> {target_lang} via Gurudev AST\n{code}"
    
    def map_types(self, type_info: Dict[str, Any], source_lang: str, target_lang: str) -> Dict[str, Any]:
        """Mapeia tipos entre linguagens"""
        
        # Mapeamento universal baseado no dodecálogo
        universal_type_map = {
            "int": {"python": "int", "javascript": "number", "java": "int", "rust": "i32"},
            "string": {"python": "str", "javascript": "string", "java": "String", "rust": "String"},
            "boolean": {"python": "bool", "javascript": "boolean", "java": "boolean", "rust": "bool"},
            "array": {"python": "list", "javascript": "Array", "java": "List", "rust": "Vec"},
            "null": {"python": "None", "javascript": "null", "java": "null", "rust": "None"}
        }
        
        mapped_types = {}
        for universal_type, lang_map in universal_type_map.items():
            if source_lang in lang_map and target_lang in lang_map:
                mapped_types[lang_map[source_lang]] = lang_map[target_lang]
        
        return mapped_types
    
    def handle_paradigm_mismatch(self, paradigm_diff: List[str]) -> Dict[str, Any]:
        """Lida com incompatibilidades paradigmáticas"""
        
        solutions = {
            "imperative": "Wrapper imperativo para encapsular funcionalidade",
            "functional": "Adaptador funcional usando higher-order functions",
            "object_oriented": "Proxy object para emular comportamento OO",
            "declarative": "DSL generator para sintaxe declarativa"
        }
        
        return {
            "paradigm_differences": paradigm_diff,
            "suggested_solutions": [solutions.get(p, f"Custom adapter for {p}") for p in paradigm_diff],
            "gurudev_principle": self.dodecalogo.get("3", "Interoperabilidade universal")
        }

class ComparativeProgrammingAnalyzer:
    """Analisador para estudos de programação comparada"""
    
    def __init__(self, db: ComparativeProgrammingDB):
        self.db = db
        self.bridge = UniversalGurudevBridge(db)
    
    def analyze_paradigm_distribution(self) -> Dict[str, Any]:
        """Analisa distribuição de paradigmas nas linguagens"""
        
        paradigm_count = {}
        for profile in self.db.profiles.values():
            for paradigm in profile.paradigms:
                paradigm_count[paradigm.value] = paradigm_count.get(paradigm.value, 0) + 1
        
        total_languages = len(self.db.profiles)
        paradigm_percentages = {
            paradigm: (count / total_languages) * 100 
            for paradigm, count in paradigm_count.items()
        }
        
        return {
            "paradigm_distribution": paradigm_count,
            "paradigm_percentages": paradigm_percentages,
            "most_common_paradigm": max(paradigm_count, key=paradigm_count.get),
            "total_languages_analyzed": total_languages
        }
    
    def generate_interop_matrix(self) -> Dict[str, Dict[str, float]]:
        """Gera matriz de compatibilidade entre todas as linguagens"""
        
        languages = list(self.db.profiles.keys())
        matrix = {}
        
        for lang1 in languages:
            matrix[lang1] = {}
            for lang2 in languages:
                if lang1 == lang2:
                    matrix[lang1][lang2] = 100.0
                else:
                    comparison = self.db.compare_languages(lang1, lang2)
                    matrix[lang1][lang2] = comparison["interoperability_score"]
        
        return matrix
    
    def recommend_learning_path(self, target_paradigms: List[str]) -> Dict[str, Any]:
        """Recomenda caminho de aprendizado baseado em paradigmas desejados"""
        
        target_paradigm_enums = [ParadigmType(p) for p in target_paradigms]
        
        # Rankeia linguagens por compatibilidade com paradigmas desejados
        language_scores = {}
        
        for lang_name, profile in self.db.profiles.items():
            common_paradigms = set(profile.paradigms) & set(target_paradigm_enums)
            score = len(common_paradigms) / len(target_paradigm_enums)
            language_scores[lang_name] = score
        
        # Ordena por score decrescente
        ranked_languages = sorted(language_scores.items(), key=lambda x: x[1], reverse=True)
        
        return {
            "target_paradigms": target_paradigms,
            "recommended_languages": ranked_languages[:5],  # Top 5
            "learning_path": [lang for lang, score in ranked_languages[:3]],
            "rationale": "Ordenado por cobertura dos paradigmas desejados"
        }

# Exemplo de uso
if __name__ == "__main__":
    # Inicializa sistema
    comp_db = ComparativeProgrammingDB()
    analyzer = ComparativeProgrammingAnalyzer(comp_db)
    
    # Análise paradigmática
    paradigm_analysis = analyzer.analyze_paradigm_distribution()
    print("Distribuição de Paradigmas:")
    print(json.dumps(paradigm_analysis, indent=2))
    
    # Comparação entre linguagens
    if len(comp_db.profiles) >= 2:
        languages = list(comp_db.profiles.keys())
        comparison = comp_db.compare_languages(languages[0], languages[1])
        print(f"\nComparação {languages[0]} vs {languages[1]}:")
        print(json.dumps(comparison, indent=2))
    
    # Matriz de interoperabilidade
    interop_matrix = analyzer.generate_interop_matrix()
    print("\nMatriz de Interoperabilidade:")
    print(json.dumps(interop_matrix, indent=2))
    
    # Recomendação de aprendizado
    learning_path = analyzer.recommend_learning_path(["functional", "object_oriented"])
    print("\nCaminho de Aprendizado Recomendado:")
    print(json.dumps(learning_path, indent=2))
