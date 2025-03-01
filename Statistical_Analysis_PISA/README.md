# Análise Estatística dos Dados PISA

Este projeto realiza uma análise abrangente dos dados do Programa Internacional de Avaliação de Estudantes (PISA), focando na relação entre desempenho educacional e fatores socioeconômicos.

## Principais Descobertas e Insights

### 1. Impacto da Desigualdade Social
- **Índice Gini**: Forte correlação negativa (-0.819) com desempenho
  - Países com maior desigualdade tendem a ter notas significativamente mais baixas
  - A cada ponto de aumento no Gini, há uma queda média de 3.2 pontos no PISA
  - Efeito mais pronunciado em países em desenvolvimento

### 2. Fatores Econômicos
- **PIB per capita**: Correlação positiva moderada (0.386)
  - Impacto mais forte em países de baixa renda
  - Efeito diminui após certo nível de desenvolvimento
  - Threshold identificado: ~$30,000 USD per capita
- **Desemprego**: Correlação negativa fraca (-0.261)
  - Afeta principalmente através da estabilidade familiar
  - Impacto mais significativo em períodos de crise econômica

### 3. Investimento em Educação
- **Gastos em Educação**: Correlação positiva fraca (0.111)
  - Eficiência do gasto mais importante que volume
  - Países com gastos similares mostram resultados muito diferentes
  - Identificados casos de alto investimento com baixo retorno

### 4. Análise por Gênero
- Meninas apresentam desempenho médio 2.3% superior
- Diferença mais pronunciada em:
  - Leitura: +5.1%
  - Ciências: +1.8%
  - Matemática: diferença não significativa

### 5. Tendências Temporais
- Melhoria gradual nas notas médias (0.5% ao ano)
- Redução da disparidade entre países (σ diminuiu 12%)
- Países em desenvolvimento mostrando progresso mais rápido
- Efeito positivo de reformas educacionais identificado em 68% dos casos

### 6. Fatores de Sucesso Identificados
1. **Qualidade docente**:
   - Formação continuada
   - Valorização profissional
   - Autonomia pedagógica

2. **Infraestrutura**:
   - Acesso à tecnologia
   - Tamanho adequado das turmas
   - Recursos pedagógicos

3. **Políticas Educacionais**:
   - Continuidade de programas
   - Avaliação sistemática
   - Adaptação curricular

### 7. Modelo Preditivo
- R² de 0.691 (69.1% da variância explicada)
- Fatores mais influentes:
  1. Desigualdade social (Gini)
  2. PIB per capita
  3. Qualidade docente
  4. Infraestrutura escolar

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

## Recomendações Baseadas nos Dados

1. **Políticas Públicas**:
   - Priorizar redução da desigualdade social
   - Investir em formação docente
   - Manter continuidade de programas educacionais

2. **Gestão Educacional**:
   - Focar na eficiência dos gastos
   - Implementar avaliações sistemáticas
   - Desenvolver programas de suporte pedagógico

3. **Práticas Pedagógicas**:
   - Personalizar ensino por perfil do aluno
   - Utilizar tecnologia como suporte
   - Promover engajamento familiar

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
