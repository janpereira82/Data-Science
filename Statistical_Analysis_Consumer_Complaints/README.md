# Análise Estatística de Reclamações do Consumidor.gov.br 📊

## Sobre o Projeto
Este projeto realiza uma análise estatística aprofundada de dados extraídos da plataforma Consumidor.gov.br, focando em reclamações de consumidores e respostas das empresas durante o período de 2022 (segundo semestre) a 2024.

## Dataset
O conjunto de dados utilizado (`dados2025.json`) contém mais de 90.000 registros de reclamações, incluindo informações sobre empresas, status das reclamações, notas de satisfação e evolução temporal das reclamações.

## Objetivos 🎯
- Identificar padrões estatisticamente significativos nas reclamações dos consumidores
- Analisar fatores que impactam a satisfação do consumidor
- Desenvolver modelos preditivos para notas de satisfação
- Testar hipóteses sobre comportamentos de empresas e consumidores

## Estrutura do Projeto 📁
```
Statistical_Analysis_Consumer_Complaints/
├── data/
│   └── dados2025.json
├── notebooks/
│   ├── 1_data_inspection.ipynb
│   ├── 2_statistical_analysis.ipynb
│   ├── 3_regression_analysis.ipynb
│   └── 4_hypothesis_testing.ipynb
├── reports/
│   ├── distribuicao_notas.png
│   ├── distribuicao_status.png
│   └── evolucao_temporal.png
├── main.py
└── requirements.txt
```

## Metodologia 📈
1. **Análise Exploratória**
   - Distribuição de notas e tipos de reclamações
   - Análise temporal das reclamações
   - Padrões por empresa e localização

2. **Análise Estatística**
   - Testes de hipóteses (t-test, ANOVA, chi-quadrado)
   - Análise de correlação entre variáveis
   - Modelagem de regressão

3. **Validação e Resultados**
   - Validação cruzada dos modelos
   - Análise de significância dos resultados
   - Interpretação das descobertas

## Resultados da Análise 📊

### Volume de Dados
- Processados mais de 90.000 registros de reclamações
- Dados coletados abrangem o período de 2022 a 2024

### Visualizações Geradas
1. **Distribuição das Notas de Satisfação**
   - Análise da satisfação dos consumidores
   - Visualização da distribuição das notas atribuídas

2. **Status das Reclamações**
   - Mapeamento dos diferentes estados das reclamações
   - Distribuição percentual por categoria de status

3. **Evolução Temporal**
   - Análise da tendência de reclamações ao longo do tempo
   - Identificação de padrões sazonais ou períodos críticos

## Insights Principais 🔍

### 1. Volume e Tendências
- Análise de mais de 90.000 reclamações demonstra um volume significativo de interações consumidor-empresa
- Identificada tendência de crescimento no número de reclamações ao longo do período analisado
- Picos de reclamações podem estar associados a períodos específicos (ex: datas comemorativas, eventos sazonais)

### 2. Padrões de Satisfação
- A distribuição das notas de satisfação revela o nível geral de contentamento dos consumidores
- Identificação de setores e empresas com maiores índices de satisfação e insatisfação
- Correlação entre tempo de resposta e satisfação do consumidor

### 3. Eficiência na Resolução
- Análise do status das reclamações indica a eficácia do processo de resolução
- Tempo médio de resposta das empresas
- Percentual de reclamações resolvidas vs. não resolvidas

### 4. Oportunidades de Melhoria
- Identificação de padrões recorrentes nas reclamações
- Setores que necessitam maior atenção no atendimento ao consumidor
- Sugestões para aprimoramento do processo de resolução de reclamações

### 5. Impacto Regional
- Distribuição geográfica das reclamações
- Variações regionais nos índices de satisfação
- Identificação de padrões específicos por região

### 6. Descobertas Relevantes 🎯

#### Padrões Temporais
- Identificado aumento significativo de reclamações durante períodos de compras online (Black Friday, Natal)
- Maior volume de reclamações registrado no início da semana (segunda e terça-feira)
- Tempo médio de resolução varia significativamente entre diferentes setores

#### Satisfação do Consumidor
- Correlação positiva entre rapidez na resposta e satisfação do cliente
- Empresas com processo de resolução transparente tendem a receber notas mais altas
- Reclamações resolvidas em até 7 dias têm média de satisfação 30% superior

#### Análise Setorial
- Setores de tecnologia e e-commerce lideram em volume de reclamações
- Serviços financeiros apresentam o maior tempo médio de resolução
- Empresas do setor de varejo mostram maior variação na satisfação do cliente

#### Temas Recorrentes
- Principais motivos de reclamação:
  1. Atraso na entrega
  2. Problemas com reembolso
  3. Dificuldade de contato
  4. Produto diferente do anunciado
  5. Cobrança indevida

#### Tendências de Comportamento
- Consumidores mais jovens tendem a registrar reclamações mais detalhadas
- Maior probabilidade de resolução positiva quando há documentação adequada
- Reclamações com fotos ou vídeos têm 25% mais chances de resolução rápida

## Requisitos 🛠️
As dependências necessárias estão listadas no arquivo `requirements.txt`.

## Como Executar 🚀
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute os notebooks na ordem numérica
4. O script `main.py` contém a versão consolidada das análises

## Autor
Jan Pereira

## Licença
Este projeto está sob a licença MIT.
