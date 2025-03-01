# Feature Engineering para Previsão de Doenças Cardíacas

## Descrição do Projeto
Este projeto realiza feature engineering no conjunto de dados Heart Disease Dataset UCI, criando novas variáveis para melhorar a performance de modelos preditivos de risco cardíaco.

## Estrutura do Projeto
```
📦 Feature Engineering for Heart Disease
┣ 📂 data
┃ ┗ 📄 HeartDiseaseTrain-Test.csv
┣ 📂 notebooks
┃ ┣ 📄 1_data_inspection.ipynb
┃ ┣ 📄 2_statistical_analysis.ipynb
┃ ┣ 📄 3_feature_engineering.ipynb
┃ ┣ 📄 4_feature_selection.ipynb
┃ ┗ 📄 5_model_evaluation.ipynb
┣ 📂 reports
┃ ┗ 📄 feature_engineering_summary.pdf
┣ 📂 src
┃ ┣ 📄 data_analysis.py
┃ ┗ 📄 feature_engineering.py
┣ 📄 README.md
┣ 📄 requirements.txt
┗ 📄 main.py
```

## Metodologia

### 1. Análise Exploratória
- Carregamento e inspeção dos dados
- Análise de estatísticas descritivas
- Visualização de distribuições e correlações

### 2. Feature Engineering
- Features de Risco por Idade
- Features de Risco por Pressão Arterial
- Índice de Estresse Cardíaco
- Score de Risco Combinado
- Features de Interação
- Codificação de Variáveis Categóricas

### 3. Seleção de Features
- Análise de correlação
- Importância via Random Forest
- Seleção baseada em domínio médico

### 4. Avaliação de Modelos
- Comparação de performance
- Validação cruzada
- Análise de importância das features

## Requisitos
Para instalar as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar
1. Clone o repositório
2. Instale as dependências
3. Execute os notebooks na ordem numérica
4. Veja os resultados na pasta reports

## Resultados
Os resultados detalhados podem ser encontrados nos notebooks e no relatório final em `reports/feature_engineering_summary.pdf`.

## Autor
[Jan Pereira](https://github.com/janpereira82)
