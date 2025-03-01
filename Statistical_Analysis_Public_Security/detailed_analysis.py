import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

class SecurityDataAnalyzer:
    def __init__(self):
        self.df_ocorrencias = None
        self.df_vitimas = None
        
    def load_data(self):
        """Carrega e prepara os dados para análise."""
        # Carregar dados
        self.df_ocorrencias = pd.read_csv('data/indicadoressegurancapublica_ocorrecia.CSV', 
                                        encoding='latin1', sep=';')
        self.df_vitimas = pd.read_csv('data/indicadoressegurancapublica_vitimas.CSV', 
                                    encoding='latin1', sep=';')
        
        # Substituir "-" por 0 e converter 'Ocorrências' para numérico
        self.df_ocorrencias['Ocorrências'] = self.df_ocorrencias['Ocorrências'].replace('-', '0')
        self.df_ocorrencias['Ocorrências'] = pd.to_numeric(self.df_ocorrencias['Ocorrências'])
        
        # Criar coluna de data
        meses = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
                'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12}
        
        for df in [self.df_ocorrencias, self.df_vitimas]:
            df['Data'] = pd.to_datetime(df['Ano'].astype(str) + '-' + 
                                      df['Mês'].map(meses).astype(str) + '-01')
    
    def analyze_crime_trends(self):
        """Analisa tendências temporais dos crimes."""
        # Análise por tipo de crime ao longo do tempo
        crimes_tempo = self.df_ocorrencias.groupby(['Data', 'Tipo Crime'])['Ocorrências'].sum().reset_index()
        
        # Criar subplots para diferentes categorias de crime
        unique_crimes = crimes_tempo['Tipo Crime'].unique()
        n_crimes = len(unique_crimes)
        n_cols = 2
        n_rows = (n_crimes + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4*n_rows))
        axes = axes.flatten()
        
        for idx, crime in enumerate(unique_crimes):
            data = crimes_tempo[crimes_tempo['Tipo Crime'] == crime]
            axes[idx].plot(data['Data'], data['Ocorrências'])
            axes[idx].set_title(crime)
            axes[idx].set_xlabel('Data')
            axes[idx].set_ylabel('Número de Ocorrências')
            axes[idx].tick_params(axis='x', rotation=45)
        
        # Remover subplots vazios
        for idx in range(n_crimes, len(axes)):
            fig.delaxes(axes[idx])
        
        plt.tight_layout()
        plt.savefig('reports/crime_trends.png')
        plt.close()
        
    def analyze_regional_distribution(self):
        """Analisa a distribuição regional dos crimes."""
        # Total de ocorrências por UF e tipo de crime
        ocorrencias_uf_crime = self.df_ocorrencias.pivot_table(
            values='Ocorrências',
            index='UF',
            columns='Tipo Crime',
            aggfunc='sum'
        )
        
        # Plotar heatmap
        plt.figure(figsize=(15, 10))
        sns.heatmap(ocorrencias_uf_crime, annot=True, fmt='.0f', cmap='YlOrRd')
        plt.title('Distribuição de Ocorrências por UF e Tipo de Crime')
        plt.xlabel('Tipo de Crime')
        plt.ylabel('UF')
        plt.tight_layout()
        plt.savefig('reports/regional_distribution.png')
        plt.close()
        
    def analyze_crime_correlation(self):
        """Analisa correlações entre diferentes tipos de crimes."""
        # Pivot table para análise de correlação
        crime_pivot = self.df_ocorrencias.pivot_table(
            index=['UF', 'Data'],
            columns='Tipo Crime',
            values='Ocorrências',
            aggfunc='sum'
        ).reset_index()
        
        # Matriz de correlação
        corr_matrix = crime_pivot.select_dtypes(include=[np.number]).corr()
        
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
        plt.title('Correlação entre Tipos de Crime')
        plt.tight_layout()
        plt.savefig('reports/crime_correlation.png')
        plt.close()
        
    def analyze_temporal_patterns(self):
        """Analisa padrões temporais nos crimes."""
        # Média de ocorrências por mês
        monthly_avg = self.df_ocorrencias.groupby('Mês')['Ocorrências'].mean()
        
        plt.figure(figsize=(12, 6))
        monthly_avg.plot(kind='bar')
        plt.title('Média de Ocorrências por Mês')
        plt.xlabel('Mês')
        plt.ylabel('Média de Ocorrências')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('reports/temporal_patterns.png')
        plt.close()
        
    def generate_summary_statistics(self):
        """Gera estatísticas resumidas dos dados."""
        # Estatísticas por tipo de crime
        crime_stats = self.df_ocorrencias.groupby('Tipo Crime').agg({
            'Ocorrências': ['count', 'mean', 'std', 'min', 'max']
        }).round(2)
        
        # Estatísticas por UF
        uf_stats = self.df_ocorrencias.groupby('UF').agg({
            'Ocorrências': ['count', 'mean', 'std', 'min', 'max']
        }).round(2)
        
        # Salvar estatísticas em CSV
        crime_stats.to_csv('reports/crime_statistics.csv')
        uf_stats.to_csv('reports/uf_statistics.csv')
        
        return crime_stats, uf_stats

def main():
    # Criar diretório de reports se não existir
    Path('reports').mkdir(exist_ok=True)
    
    # Inicializar e executar análises
    analyzer = SecurityDataAnalyzer()
    analyzer.load_data()
    
    print("Gerando análises...")
    analyzer.analyze_crime_trends()
    analyzer.analyze_regional_distribution()
    analyzer.analyze_crime_correlation()
    analyzer.analyze_temporal_patterns()
    
    crime_stats, uf_stats = analyzer.generate_summary_statistics()
    
    print("\nEstatísticas por Tipo de Crime:")
    print(crime_stats)
    print("\nEstatísticas por UF:")
    print(uf_stats)
    
    print("\nAnálise concluída! Os resultados foram salvos na pasta 'reports'.")

if __name__ == "__main__":
    main()
