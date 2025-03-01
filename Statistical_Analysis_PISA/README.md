# Análise Estatística dos Dados PISA

Este projeto realiza uma análise abrangente dos dados do Programa Internacional de Avaliação de Estudantes (PISA), focando na relação entre desempenho educacional e fatores socioeconômicos.

## Estrutura do Projeto

```
Statistical_Analysis_PISA/
├── data/
│   └── economics_and_education_dataset_CSV.csv
├── notebooks/
│   ├── 1_data_inspection.ipynb
│   ├── 2_statistical_analysis.ipynb
│   ├── 3_regression_analysis.ipynb
│   └── 4_hypothesis_testing.ipynb
├── src/
│   ├── pisa_analysis.py
│   └── analysis_utils.py
└── requirements.txt
```

## Notebooks de Análise

### 1. Inspeção de Dados
- Análise exploratória inicial
- Tratamento de valores ausentes
- Estatísticas descritivas básicas
- Visualizações preliminares
- Análise temporal básica

### 2. Análise Estatística
- Testes de normalidade
- Análise de diferenças entre grupos
- Correlações detalhadas
- Análise de tendências
- ANOVA multifatorial

### 3. Análise de Regressão
- Preparação de features
- Modelos de regressão linear
- Análise de coeficientes
- Validação cruzada
- Análise de resíduos
- Comparação de modelos

### 4. Testes de Hipóteses
- Diferenças entre sexos
- Efeito do PIB no desempenho
- Correlação com gastos em educação
- Análise de tendências temporais
- Interações entre variáveis

## Principais Descobertas

1. **Correlações Significativas**:
   - Índice Gini: correlação negativa forte (-0.819)
   - PIB per capita: correlação positiva moderada (0.386)
   - Gastos em educação: correlação positiva fraca (0.111)

2. **Modelo de Regressão**:
   - R² de 0.691 (69.1% da variância explicada)
   - Fatores mais influentes: desigualdade social e PIB per capita

3. **Análises Estatísticas**:
   - Diferenças significativas entre países
   - Impacto variável dos gastos em educação
   - Tendências temporais identificadas

## Instalação e Uso

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Statistical_Analysis_PISA.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute os notebooks na ordem numérica:
   - Comece com `1_data_inspection.ipynb`
   - Siga para análises mais complexas nos notebooks subsequentes

## Dependências

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- statsmodels
- scikit-learn

## Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
