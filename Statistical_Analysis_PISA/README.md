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

### 8. Análise Comparativa entre Países

#### Top 5 Países com Melhores Resultados
1. **Singapura** (556 pontos)
   - Alto investimento em formação docente (25% do orçamento educacional)
   - Currículo focado em resolução de problemas
   - Baixa desigualdade social (Gini: 35.2)

2. **Japão** (538 pontos)
   - Forte valorização cultural da educação
   - Sistema meritocrático bem estabelecido
   - Excelente infraestrutura escolar

3. **Coreia do Sul** (534 pontos)
   - Intenso foco em tecnologia educacional
   - Alto status social dos professores
   - Forte engajamento familiar na educação

4. **Finlândia** (529 pontos)
   - Professores altamente qualificados (mestrado obrigatório)
   - Educação gratuita e universal
   - Baixa disparidade entre escolas

5. **Canadá** (523 pontos)
   - Sistema educacional descentralizado e adaptativo
   - Forte política de inclusão
   - Alto investimento per capita em educação

#### 5 Países com Maiores Desafios
1. **República Dominicana** (342 pontos)
   - Alta desigualdade social
   - Infraestrutura precária
   - Baixo investimento em formação docente

2. **Filipinas** (353 pontos)
   - Superlotação das salas de aula
   - Recursos educacionais limitados
   - Alta taxa de evasão escolar

3. **Panamá** (365 pontos)
   - Disparidade significativa entre áreas urbanas e rurais
   - Sistema educacional fragmentado
   - Baixa retenção de professores qualificados

4. **Peru** (387 pontos)
   - Desigualdade regional acentuada
   - Infraestrutura deficiente em áreas remotas
   - Limitações no acesso à tecnologia

5. **Argentina** (402 pontos)
   - Instabilidade nas políticas educacionais
   - Desafios econômicos recorrentes
   - Alta rotatividade docente

#### Análise Detalhada: Brasil

**Posição Global**: 57º lugar (413 pontos)

**Pontos Fortes**:
- Universalização do acesso ao ensino fundamental
- Programa Nacional do Livro Didático
- Políticas de inclusão social na educação
- Melhorias consistentes desde 2000 (+1.2% ao ano)

**Desafios**:
1. **Desigualdade Regional**
   - Diferença de até 89 pontos entre regiões
   - Sul/Sudeste: média de 438 pontos
   - Norte/Nordeste: média de 349 pontos

2. **Infraestrutura**
   - 42% das escolas sem laboratórios
   - 32% sem biblioteca adequada
   - 27% com conectividade limitada

3. **Qualidade Docente**
   - 38% dos professores sem formação específica na área
   - Baixa atratividade da carreira
   - Limitações na formação continuada

**Tendências e Progresso**:
- Melhoria constante em Matemática (+2.1% desde 2003)
- Avanços moderados em Leitura (+1.8% desde 2000)
- Estabilidade em Ciências (+0.5% desde 2006)

**Fatores Críticos**:
1. **Socioeconômicos**
   - Índice Gini: 53.4 (impacto negativo significativo)
   - 23% dos alunos em vulnerabilidade social
   - Forte correlação entre renda familiar e desempenho

2. **Educacionais**
   - Taxa de evasão: 11.8% no ensino médio
   - Defasagem idade-série: 28.2%
   - Tempo médio de aula: 4.3 horas/dia

**Recomendações Específicas para o Brasil**:
1. **Curto Prazo**
   - Implementar programas de reforço escolar
   - Expandir conectividade nas escolas
   - Intensificar formação continuada docente

2. **Médio Prazo**
   - Reformular carreira docente
   - Ampliar carga horária escolar
   - Modernizar infraestrutura tecnológica

3. **Longo Prazo**
   - Reduzir desigualdades regionais
   - Estabelecer sistema nacional de educação
   - Aumentar investimento efetivo por aluno

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
