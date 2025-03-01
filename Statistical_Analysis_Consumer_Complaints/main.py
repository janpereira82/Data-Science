import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
from pathlib import Path
import ijson  # Para processar JSON grandes

def load_and_process_data():
    """
    Carrega e processa os dados do arquivo JSON grande
    """
    # Carregar dados do JSON em chunks
    data_path = Path('data/dados2025.json')
    
    # Lista para armazenar os chunks de dados
    data_chunks = []
    chunk_size = 1000
    current_chunk = []
    
    try:
        with open(data_path, 'rb') as f:
            parser = ijson.items(f, 'item')
            
            for i, record in enumerate(parser):
                current_chunk.append(record)
                
                if len(current_chunk) >= chunk_size:
                    data_chunks.append(pd.DataFrame(current_chunk))
                    current_chunk = []
                    
                if i % 10000 == 0:
                    print(f"Processados {i} registros...")
            
            # Adicionar o último chunk se houver dados restantes
            if current_chunk:
                data_chunks.append(pd.DataFrame(current_chunk))
        
        # Concatenar todos os chunks
        df = pd.concat(data_chunks, ignore_index=True)
        
        # Converter data para datetime se existir
        if 'data' in df.columns:
            df['data'] = pd.to_datetime(df['data'])
        
        return df
    
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return None

def analyze_basic_stats(df):
    """
    Realiza análise estatística básica dos dados
    """
    print("\n=== Análise Básica dos Dados ===")
    print(f"Número total de reclamações: {len(df)}")
    print("\nInformações do Dataset:")
    print(df.info())
    
    print("\nEstatísticas Descritivas:")
    print(df.describe())
    
    # Contagem de reclamações por empresa (top 10)
    if 'empresa' in df.columns:
        print("\nTop 10 Empresas com Mais Reclamações:")
        print(df['empresa'].value_counts().head(10))

def analyze_satisfaction(df):
    """
    Analisa as notas de satisfação
    """
    if 'nota' not in df.columns:
        print("Coluna 'nota' não encontrada no dataset")
        return
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='nota', bins=5)
    plt.title('Distribuição das Notas de Satisfação')
    plt.xlabel('Nota')
    plt.ylabel('Frequência')
    plt.savefig('reports/distribuicao_notas.png')
    plt.close()

def analyze_temporal_patterns(df):
    """
    Analisa padrões temporais nas reclamações
    """
    if 'data' not in df.columns:
        print("Coluna 'data' não encontrada no dataset")
        return
    
    # Análise temporal
    reclamacoes_por_mes = df.groupby(df['data'].dt.to_period('M')).size()
    
    plt.figure(figsize=(12, 6))
    reclamacoes_por_mes.plot(kind='line')
    plt.title('Evolução do Número de Reclamações ao Longo do Tempo')
    plt.xlabel('Mês')
    plt.ylabel('Número de Reclamações')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/evolucao_temporal.png')
    plt.close()

def analyze_status_distribution(df):
    """
    Analisa a distribuição dos status das reclamações
    """
    if 'status' not in df.columns:
        print("Coluna 'status' não encontrada no dataset")
        return
    
    plt.figure(figsize=(10, 6))
    df['status'].value_counts().plot(kind='bar')
    plt.title('Distribuição dos Status das Reclamações')
    plt.xlabel('Status')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/distribuicao_status.png')
    plt.close()

def analyze_insights(df):
    """
    Extrai insights importantes dos dados
    """
    insights = {
        'total_reclamacoes': len(df),
        'periodo': {
            'inicio': df['data'].min(),
            'fim': df['data'].max()
        }
    }
    
    # Análise por empresa
    if 'empresa' in df.columns:
        empresas_mais_reclamadas = df['empresa'].value_counts().head(5)
        insights['top_empresas'] = empresas_mais_reclamadas.to_dict()
    
    # Análise de satisfação
    if 'nota' in df.columns:
        insights['satisfacao'] = {
            'media': df['nota'].mean(),
            'mediana': df['nota'].median(),
            'moda': df['nota'].mode().iloc[0] if not df['nota'].mode().empty else None
        }
    
    # Análise temporal
    if 'data' in df.columns:
        df['mes_ano'] = df['data'].dt.to_period('M')
        reclamacoes_mes = df.groupby('mes_ano').size()
        insights['temporal'] = {
            'mes_mais_reclamacoes': str(reclamacoes_mes.idxmax()),
            'quantidade_max': int(reclamacoes_mes.max())
        }
    
    # Análise de status
    if 'status' in df.columns:
        status_counts = df['status'].value_counts()
        insights['status'] = status_counts.to_dict()
    
    return insights

def analyze_detailed_insights(df):
    """
    Realiza uma análise mais detalhada dos dados para extrair insights específicos
    """
    insights = {}
    
    # Análise de Satisfação por Status
    if 'nota' in df.columns and 'status' in df.columns:
        satisfacao_por_status = df.groupby('status')['nota'].agg(['mean', 'count']).round(2)
        satisfacao_por_status = satisfacao_por_status.sort_values('count', ascending=False)
        insights['satisfacao_por_status'] = satisfacao_por_status.to_dict('index')
    
    # Análise Temporal Detalhada
    if 'data' in df.columns:
        df['mes'] = df['data'].dt.month
        df['ano'] = df['data'].dt.year
        reclamacoes_por_mes = df.groupby(['ano', 'mes']).size()
        insights['tendencia_temporal'] = {
            f"{ano}-{mes:02d}": int(count)
            for (ano, mes), count in reclamacoes_por_mes.items()
        }
    
    # Análise de Palavras Comuns nos Comentários
    if 'comentario' in df.columns:
        from collections import Counter
        import re
        
        def clean_text(text):
            if isinstance(text, str):
                # Remove caracteres especiais e converte para minúsculas
                text = re.sub(r'[^\w\s]', '', text.lower())
                # Remove palavras comuns (stopwords)
                stopwords = {'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas'}
                return ' '.join(word for word in text.split() if word not in stopwords and len(word) > 3)
            return ''
        
        # Processa os comentários
        all_words = ' '.join(df['comentario'].apply(clean_text).dropna())
        word_counts = Counter(all_words.split())
        insights['palavras_frequentes'] = dict(word_counts.most_common(20))
    
    # Análise de Correlações
    if 'nota' in df.columns and 'status' in df.columns:
        # Converter status para numérico para análise de correlação
        status_map = {status: i for i, status in enumerate(df['status'].unique())}
        df['status_num'] = df['status'].map(status_map)
        
        correlacoes = {}
        for col in ['status_num']:
            if col in df.columns:
                corr = df['nota'].corr(df[col])
                correlacoes[f'nota_vs_{col}'] = round(corr, 3)
        
        insights['correlacoes'] = correlacoes
    
    return insights

def main():
    # Configurações básicas de visualização
    sns.set()
    
    # Criar diretório de reports se não existir
    Path('reports').mkdir(exist_ok=True)
    
    try:
        # Carregar e processar dados
        print("Carregando dados...")
        df = load_and_process_data()
        
        if df is not None:
            # Realizar análises básicas
            analyze_basic_stats(df)
            analyze_satisfaction(df)
            analyze_temporal_patterns(df)
            analyze_status_distribution(df)
            
            # Realizar análise detalhada
            print("\nRealizando análise detalhada...")
            detailed_insights = analyze_detailed_insights(df)
            
            # Salvar insights em um arquivo JSON
            with open('reports/detailed_insights.json', 'w', encoding='utf-8') as f:
                json.dump(detailed_insights, f, ensure_ascii=False, indent=4, default=str)
            
            print("\nAnálise concluída! Os resultados foram salvos na pasta 'reports'.")
        
    except FileNotFoundError:
        print("Erro: Arquivo de dados não encontrado em 'data/dados2025.json'")
    except Exception as e:
        print(f"Erro durante a análise: {str(e)}")

if __name__ == "__main__":
    main()
