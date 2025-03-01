"""
Script principal para execução do pipeline de Feature Engineering
"""

from src.data_analysis import HeartDiseaseAnalysis
from src.feature_engineering import HeartDiseaseFeatureEngineering

def main():
    # Inicializar análise de dados
    print("Iniciando análise de dados...")
    data_analysis = HeartDiseaseAnalysis()
    data_analysis.run_analysis()
    
    # Realizar feature engineering
    print("\nIniciando feature engineering...")
    feature_engineering = HeartDiseaseFeatureEngineering()
    feature_engineering.process_features()
    feature_engineering.evaluate_features()

if __name__ == "__main__":
    main()
