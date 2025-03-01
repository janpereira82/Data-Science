# Análise Exploratória do Dataset Ames Housing

## Objetivo
Este projeto realiza uma análise exploratória detalhada do conjunto de dados Ames Housing, que contém informações sobre preços de imóveis em Ames, Iowa. O objetivo é extrair insights valiosos sobre os fatores que influenciam os preços dos imóveis e preparar os dados para futura modelagem.

## Principais Insights

### 1. Análise de Preços
- A distribuição dos preços de venda é assimétrica à direita, com média de $180,921 e mediana de $163,000
- Transformação logarítmica dos preços resulta em uma distribuição mais normal
- 75% das casas têm preço abaixo de $220,000

### 2. Fatores mais Correlacionados com Preço
1. Qualidade Geral (Overall Quality): 0.79
2. Área Habitável Acima do Solo (GrLivArea): 0.71
3. Área Total do Porão (TotalBsmtSF): 0.63
4. Ano de Construção (YearBuilt): 0.58
5. Área da Garagem (GarageArea): 0.54

### 3. Características do Imóvel
- Casas mais novas tendem a ter preços mais altos
- Bairros com preços mais elevados: NorthRidge, NorthRidgeHt, StoneBr
- Qualidade da cozinha e acabamento exterior têm forte influência no preço

### 4. Engenharia de Features
- Criadas novas features como área total, idade da casa e qualidade geral
- Features numéricas com alta assimetria foram transformadas usando log
- Variáveis categóricas foram codificadas usando Label Encoding e One-Hot Encoding

## Estrutura do Projeto
```markdown
📦 Ames_Housing_EDA
 ┣ 📂 data
 ┃ ┣ 📄 ames_housing.csv
 ┣ 📂 notebooks
 ┃ ┣ 📄 1_data_inspection.ipynb
 ┃ ┣ 📄 2_statistical_analysis.ipynb
 ┃ ┣ 📄 3_missing_values_treatment.ipynb
 ┃ ┣ 📄 4_visualizations.ipynb
 ┃ ┣ 📄 5_feature_engineering.ipynb
 ┣ 📂 reports
 ┃ ┣ 📄 exploratory_analysis.pdf
 ┣ 📄 README.md
 ┣ 📄 requirements.txt
 ┣ 📄 main.py
```

## Metodologia
A análise está dividida em cinco etapas principais:

1. **Inspeção Inicial dos Dados**: Análise da estrutura do dataset, tipos de dados e visão geral das variáveis.
2. **Análise Estatística**: Estatísticas descritivas e distribuições das variáveis principais.
3. **Tratamento de Valores Ausentes**: Identificação e tratamento de dados faltantes.
4. **Visualizações**: Análises gráficas das relações entre variáveis.
5. **Engenharia de Features**: Preparação e transformação de dados para modelagem.

## Instalação e Uso
1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute os notebooks na ordem numérica apresentada

## Principais Bibliotecas Utilizadas
- pandas: Manipulação e análise de dados
- numpy: Computação numérica
- matplotlib/seaborn: Visualização de dados
- scikit-learn: Pré-processamento de dados
- plotly: Visualizações interativas

## Conclusões
1. A qualidade geral da casa é o fator mais importante na determinação do preço
2. A localização (bairro) tem forte influência nos preços
3. Casas mais novas e maiores tendem a ser mais valorizadas
4. Melhorias na cozinha e acabamento exterior podem aumentar significativamente o valor do imóvel
5. O dataset está bem preparado para futuros projetos de modelagem preditiva

## Autor
[Jan Pereira](https://github.com/janpereira82)
