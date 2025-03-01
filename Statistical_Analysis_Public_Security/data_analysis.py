import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configuração para exibir todas as colunas
pd.set_option('display.max_columns', None)

def load_and_inspect_data():
    """Carrega e realiza inspeção inicial dos dados."""
    # Carregar dados
    ocorrencias_path = Path('data/indicadoressegurancapublica_ocorrecia.CSV')
    vitimas_path = Path('data/indicadoressegurancapublica_vitimas.CSV')
    
    df_ocorrencias = pd.read_csv(ocorrencias_path, encoding='latin1', sep=';')
    df_vitimas = pd.read_csv(vitimas_path, encoding='latin1', sep=';')
    
    print("\n=== Análise do DataFrame de Ocorrências ===")
    print("\nPrimeiras linhas:")
    print(df_ocorrencias.head())
    print("\nInformações do DataFrame:")
    print(df_ocorrencias.info())
    print("\nEstatísticas descritivas:")
    print(df_ocorrencias.describe())
    
    print("\n=== Análise do DataFrame de Vítimas ===")
    print("\nPrimeiras linhas:")
    print(df_vitimas.head())
    print("\nInformações do DataFrame:")
    print(df_vitimas.info())
    print("\nEstatísticas descritivas:")
    print(df_vitimas.describe())
    
    return df_ocorrencias, df_vitimas

if __name__ == "__main__":
    df_ocorrencias, df_vitimas = load_and_inspect_data()
