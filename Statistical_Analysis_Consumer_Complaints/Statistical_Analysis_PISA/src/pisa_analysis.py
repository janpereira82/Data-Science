import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os
import json

def analyze_pisa_data(data_path):
    """Realiza análise completa dos dados do PISA."""
    # Carrega dados
    df = pd.read_csv(data_path)
    
    # Análise básica
    basic_stats = {
        'total_countries': df['country'].nunique(),
        'year_range': (int(df['time'].min()), int(df['time'].max())),
        'avg_rating': float(df['rating'].mean()),
        'rating_std': float(df['rating'].std())
    }
    
    # Análise de gastos em educação
    education_spending = {
        'correlation': float(df['expenditure_on _education_pct_gdp'].corr(df['rating'])),
        'avg_by_spending_level': df.groupby(pd.qcut(
            df['expenditure_on _education_pct_gdp'], 
            q=4, 
            labels=['Low', 'Medium-Low', 'Medium-High', 'High']
        ))['rating'].mean().to_dict()
    }
    
    # Análise socioeconômica
    socioeconomic_factors = {
        col: float(df[col].corr(df['rating']))
        for col in ['gini_index', 'gdp_per_capita_ppp', 'unemployment', 'urban_population_pct_total']
    }
    
    # Modelo de regressão
    features = [
        'expenditure_on _education_pct_gdp',
        'gdp_per_capita_ppp',
        'gini_index',
        'unemployment',
        'urban_population_pct_total'
    ]
    
    model_data = df.dropna(subset=features + ['rating'])
    X = model_data[features]
    y = model_data['rating']
    
    # Normaliza features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split e treino
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    model_results = {
        'r2_score': float(r2_score(y_test, y_pred)),
        'mse': float(mean_squared_error(y_test, y_pred)),
        'feature_importance': dict(zip(features, map(float, model.coef_)))
    }
    
    # Gera gráfico de tendências
    plt.figure(figsize=(12, 6))
    yearly_avg = df.groupby('time')['rating'].mean()
    plt.plot(yearly_avg.index, yearly_avg.values, marker='o')
    plt.title('Tendência de Desempenho no PISA ao Longo do Tempo')
    plt.xlabel('Ano')
    plt.ylabel('Pontuação Média')
    plt.grid(True)
    
    # Cria diretório reports se não existir
    os.makedirs('../reports', exist_ok=True)
    
    # Salva gráfico
    plt.savefig('../reports/performance_trends.png')
    plt.close()
    
    # Prepara relatório final
    report = {
        'basic_statistics': basic_stats,
        'education_spending_analysis': education_spending,
        'socioeconomic_factors': socioeconomic_factors,
        'regression_model': model_results
    }
    
    # Salva relatório
    with open('../reports/analysis_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    return report

if __name__ == "__main__":
    data_path = '../data/economics_and_education_dataset_CSV.csv'
    results = analyze_pisa_data(data_path)
    print("Análise completa! Resultados salvos em reports/")
    
    # Mostra alguns resultados principais
    print("\nEstatísticas Básicas:")
    print(f"Total de países: {results['basic_statistics']['total_countries']}")
    print(f"Anos analisados: {results['basic_statistics']['year_range']}")
    print(f"Média geral: {results['basic_statistics']['avg_rating']:.2f}")
    
    print("\nCorrelações com desempenho:")
    print(f"Gastos em educação: {results['education_spending_analysis']['correlation']:.3f}")
    for factor, corr in results['socioeconomic_factors'].items():
        print(f"{factor}: {corr:.3f}")
    
    print("\nDesempenho do modelo:")
    print(f"R² Score: {results['regression_model']['r2_score']:.3f}")
    print(f"MSE: {results['regression_model']['mse']:.3f}")
