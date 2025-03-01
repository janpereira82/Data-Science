# Análise Estatística de Dados de Segurança Pública

## 📊 Sobre o Projeto
Este projeto realiza uma análise estatística abrangente dos dados de segurança pública extraídos do SinespJC e Sinesp Integração, focando em diversos tipos de ocorrências criminais, incluindo estupro, furto de veículos, homicídio doloso, entre outros.

## 🎯 Objetivos
- Identificar padrões estatísticos em diferentes categorias criminais
- Analisar correlações entre variáveis socioeconômicas e ocorrências
- Desenvolver modelos preditivos para diferentes tipos de crimes
- Testar hipóteses sobre fatores que influenciam a criminalidade

## 📈 Insights e Resultados da Análise

### Principais Descobertas

1. **Padrões de Crimes Patrimoniais**
   - Furto de veículo: média de 765.97 ocorrências
   - Roubo de veículo: média de 727.03 ocorrências
   - Maior incidência em estados mais populosos e urbanizados

2. **Crimes Contra a Pessoa**
   - Homicídio doloso: média de 145.76 ocorrências
   - Tentativa de homicídio: média de 118.80 ocorrências
   - Distribuição mais uniforme entre os estados

3. **Crimes de Menor Frequência**
   - Lesão corporal seguida de morte: média de 2.63 ocorrências
   - Roubo a instituição financeira: média de 2.71 ocorrências
   - Roubo seguido de morte (latrocínio): média de 6.18 ocorrências

4. **Variabilidade Regional**
   - Estados mais populosos apresentam maior variação nos dados
   - Crimes patrimoniais mostram maior variabilidade que crimes contra a pessoa
   - Padrões sazonais identificados em determinados tipos de crime

## 🏆 Ranking dos Estados

### Top 5 Estados por Média de Ocorrências
1. **São Paulo**
   - Média: 1,803.18 ocorrências
   - Maior variabilidade (Desvio Padrão: 2,880.35)
   - Concentração em crimes patrimoniais

2. **Rio de Janeiro**
   - Média: 735.58 ocorrências
   - Alta variabilidade (Desvio Padrão: 1,107.74)
   - Destaque em roubos de veículos

3. **Minas Gerais**
   - Média: 408.60 ocorrências
   - Variabilidade moderada (Desvio Padrão: 642.85)
   - Distribuição mais equilibrada entre tipos de crime

4. **Rio Grande do Sul**
   - Média: 360.07 ocorrências
   - Desvio Padrão: 535.07
   - Forte incidência de furtos

5. **Paraná**
   - Média: 346.15 ocorrências
   - Desvio Padrão: 490.93
   - Padrão similar ao Rio Grande do Sul

### Estados com Menores Índices
- **Roraima**: 16.01 ocorrências (média)
- **Acre**: 14.57 ocorrências (média)
- **Amapá**: 19.49 ocorrências (média)

## 📁 Estrutura do Projeto
```
📦 Statistical_Analysis_Public_Security
 ┣ 📂 data
 ┃ ┗ 📄 public_security_data.csv
 ┣ 📂 notebooks
 ┃ ┣ 📄 1_data_inspection.ipynb
 ┃ ┣ 📄 2_statistical_analysis.ipynb
 ┃ ┣ 📄 3_regression_analysis.ipynb
 ┃ ┗ 📄 4_hypothesis_testing.ipynb
 ┣ 📂 reports
 ┃ ┗ 📄 statistical_analysis_summary.pdf
 ┣ 📄 README.md
 ┣ 📄 requirements.txt
 ┗ 📄 main.py
```

## 🔍 Metodologia
1. **Análise Exploratória**
   - Estatísticas descritivas
   - Análise de distribuições
   - Correlações entre variáveis

2. **Análise Estatística**
   - Testes de hipóteses
   - Análise de variância (ANOVA)
   - Testes qui-quadrado

3. **Modelagem Preditiva**
   - Regressão linear/múltipla
   - Validação cruzada
   - Análise de performance

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📝 Como Usar
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute os notebooks na ordem numérica
4. Consulte o relatório final em `reports/statistical_analysis_summary.pdf`

## 📄 Licença
Este projeto está sob a licença MIT.

## Autor
[Jan Pereira](https://github.com/janpereira82)
