import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class PISAAnalysis:
    def __init__(self, data_path):
        """Inicializa a análise com o dataset do PISA."""
        self.data = pd.read_csv(data_path)
        self.prepare_data()
        
    def prepare_data(self):
        """Prepara os dados para análise."""
        # Renomeia colunas para remover espaços extras
        self.data.columns = [col.strip().replace(' ', '_') for col in self.data.columns]
        
        # Cria features agregadas
        self.data['education_gdp_ratio'] = (
            self.data['expenditure_on_education_pct_gdp'] / 
            self.data['gdp_per_capita_ppp']
        )
        
        # Categoriza países por nível de desenvolvimento
        gdp_median = self.data['gdp_per_capita_ppp'].median()
        self.data['development_level'] = np.where(
            self.data['gdp_per_capita_ppp'] > gdp_median,
            'High_Income',
            'Low_Income'
        )
    
    def get_basic_stats(self):
        """Retorna estatísticas básicas do dataset."""
        return {
            'total_countries': self.data['country'].nunique(),
            'year_range': (self.data['time'].min(), self.data['time'].max()),
            'avg_rating': self.data['rating'].mean(),
            'rating_std': self.data['rating'].std()
        }
    
    def analyze_education_spending(self):
        """Analisa relação entre gastos em educação e desempenho."""
        correlation = self.data['expenditure_on_education_pct_gdp'].corr(
            self.data['rating']
        )
        
        # Agrupa por nível de gasto em educação
        spending_groups = pd.qcut(
            self.data['expenditure_on_education_pct_gdp'],
            q=4,
            labels=['Low', 'Medium-Low', 'Medium-High', 'High']
        )
        
        performance_by_spending = self.data.groupby(spending_groups)['rating'].mean()
        
        return {
            'correlation': correlation,
            'performance_by_spending': performance_by_spending.to_dict()
        }
    
    def analyze_socioeconomic_factors(self):
        """Analisa fatores socioeconômicos e sua relação com desempenho."""
        socioeconomic_cols = [
            'gini_index',
            'gdp_per_capita_ppp',
            'unemployment',
            'urban_population_pct_total'
        ]
        
        correlations = {
            col: self.data[col].corr(self.data['rating'])
            for col in socioeconomic_cols
        }
        
        return correlations
    
    def create_regression_model(self):
        """Cria modelo de regressão para prever notas."""
        features = [
            'expenditure_on_education_pct_gdp',
            'gdp_per_capita_ppp',
            'gini_index',
            'unemployment',
            'urban_population_pct_total'
        ]
        
        # Remove linhas com valores ausentes
        model_data = self.data.dropna(subset=features + ['rating'])
        
        # Prepara features e target
        X = model_data[features]
        y = model_data['rating']
        
        # Normaliza features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Split dados
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        # Treina modelo
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Avalia modelo
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        
        # Prepara coeficientes
        feature_importance = dict(zip(features, model.coef_))
        
        return {
            'r2_score': r2,
            'mse': mse,
            'feature_importance': feature_importance
        }
    
    def plot_performance_trends(self, save_path=None):
        """Plota tendências de desempenho ao longo do tempo."""
        plt.figure(figsize=(12, 6))
        
        # Média por ano
        yearly_avg = self.data.groupby('time')['rating'].mean()
        
        plt.plot(yearly_avg.index, yearly_avg.values, marker='o')
        plt.title('Tendência de Desempenho no PISA ao Longo do Tempo')
        plt.xlabel('Ano')
        plt.ylabel('Pontuação Média')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()
    
    def generate_summary_report(self):
        """Gera relatório resumido da análise."""
        basic_stats = self.get_basic_stats()
        education_analysis = self.analyze_education_spending()
        socioeconomic = self.analyze_socioeconomic_factors()
        model_results = self.create_regression_model()
        
        report = {
            'basic_statistics': basic_stats,
            'education_spending_analysis': education_analysis,
            'socioeconomic_factors': socioeconomic,
            'regression_model': model_results
        }
        
        return report
