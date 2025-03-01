from analysis_utils import PISAAnalysis
import json
import os

def main():
    # Inicializa análise
    data_path = '../data/economics_and_education_dataset_CSV.csv'
    analysis = PISAAnalysis(data_path)
    
    # Cria diretório para resultados se não existir
    os.makedirs('../reports', exist_ok=True)
    
    # Gera relatório
    report = analysis.generate_summary_report()
    
    # Salva relatório em JSON
    with open('../reports/analysis_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    
    # Gera gráfico de tendências
    analysis.plot_performance_trends('../reports/performance_trends.png')
    
    print("Análise completa! Resultados salvos em reports/")

if __name__ == "__main__":
    main()
