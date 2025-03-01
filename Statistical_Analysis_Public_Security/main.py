import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

class SecurityDataAnalyzer:
    def __init__(self, data_path):
        """Inicializa o analisador com o caminho para os dados."""
        self.data_path = Path(data_path)
        self.data = None
        
    def load_data(self):
        """Carrega os dados do arquivo CSV."""
        try:
            self.data = pd.read_csv(self.data_path)
            print("Dados carregados com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False
            
    def perform_descriptive_analysis(self):
        """Realiza análise descritiva dos dados."""
        if self.data is None:
            print("Dados não carregados!")
            return
            
        stats = self.data.describe()
        correlations = self.data.corr()
        
        return stats, correlations
        
    def test_hypotheses(self, variable, group_by):
        """Realiza testes de hipóteses."""
        if self.data is None:
            return None
            
        groups = [group for _, group in self.data.groupby(group_by)[variable]]
        f_stat, p_value = stats.f_oneway(*groups)
        
        return {'f_statistic': f_stat, 'p_value': p_value}
        
    def build_regression_model(self, target, features):
        """Constrói modelo de regressão."""
        if self.data is None:
            return None
            
        X = self.data[features]
        y = self.data[target]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        predictions = model.predict(X_test)
        
        results = {
            'r2_score': r2_score(y_test, predictions),
            'mse': mean_squared_error(y_test, predictions),
            'coefficients': dict(zip(features, model.coef_))
        }
        
        return results

def main():
    """Função principal para executar a análise."""
    data_path = Path('data/public_security_data.csv')
    analyzer = SecurityDataAnalyzer(data_path)
    
    if not analyzer.load_data():
        return
        
    # Análise descritiva
    stats, corr = analyzer.perform_descriptive_analysis()
    print("\nEstatísticas Descritivas:")
    print(stats)
    
    # Resultados serão expandidos quando os dados estiverem disponíveis
    
if __name__ == "__main__":
    main()
