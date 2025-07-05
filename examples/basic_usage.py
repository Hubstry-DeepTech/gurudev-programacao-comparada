#!/usr/bin/env python3
"""
Exemplo básico de uso da biblioteca Gurudev
"""

from gurudev import ComparativeProgrammingDB, ComparativeProgrammingAnalyzer, UniversalGurudevBridge

def main():
    print("🚀 Gurudev Comparative Programming - Exemplo Básico")
    print("=" * 50)
    
    # Inicializar sistema
    db = ComparativeProgrammingDB()
    analyzer = ComparativeProgrammingAnalyzer(db)
    bridge = UniversalGurudevBridge(db)
    
    # Listar linguagens disponíveis
    print("\n📋 Linguagens disponíveis:")
    for lang in db.profiles.keys():
        print(f"  - {lang}")
    
    # Comparar duas linguagens
    print("\n🔍 Comparando Python vs JavaScript:")
    comparison = db.compare_languages("python", "javascript")
    print(f"  Compatibilidade: {comparison['interoperability_score']}")
    print(f"  Paradigmas comuns: {comparison['paradigmatic_analysis']['common_paradigms']}")
    
    # Análise de paradigmas
    print("\n📊 Análise de Paradigmas:")
    paradigm_analysis = analyzer.analyze_paradigm_distribution()
    print(f"  Paradigma mais comum: {paradigm_analysis['most_common_paradigm']}")
    
    # Exemplo de tradução
    print("\n🔄 Tradução Python → JavaScript:")
    python_code = "def hello(name): return f'Hello, {name}!'"
    js_code = bridge.translate_syntax(python_code, "python", "javascript")
    print(f"  Python: {python_code}")
    print(f"  JavaScript: {js_code}")
    
    # Recomendação de aprendizado
    print("\n🎓 Recomendação de Aprendizado:")
    learning_path = analyzer.recommend_learning_path(["functional", "object_oriented"])
    print(f"  Para paradigmas funcionais e OO:")
    for lang, score in learning_path["recommended_languages"][:3]:
        print(f"    {lang}: {score:.2f}")

if __name__ == "__main__":
    main()
