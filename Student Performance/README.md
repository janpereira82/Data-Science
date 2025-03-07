# Análise de Desempenho dos Estudantes

## Sobre o Projeto

Este projeto realiza uma análise detalhada do desempenho acadêmico dos estudantes, utilizando técnicas de análise exploratória de dados e machine learning em R. O projeto inclui visualizações interativas e um modelo preditivo de alto desempenho para prever as notas finais dos alunos.

## Pré-requisitos

### Instalação do R

Para utilizar este projeto, siga os passos abaixo para instalar e configurar o R no seu sistema:

1. **Baixar e Instalar o R**  
   - Acesse o site oficial do R: [https://cran.r-project.org/](https://cran.r-project.org/)
   - Escolha a versão compatível com seu sistema operacional (Windows, macOS, Linux).
   - Siga as instruções de instalação padrão.

2. **Instalar o RStudio (Opcional, mas Recomendado)**  
   - Baixe o RStudio em: [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)
   - Instale seguindo as instruções do instalador.

3. **Verificar a Instalação**  
   - Abra o R ou RStudio e execute:
     ```r
     version
     ```
   - Isso exibirá a versão instalada do R.

4. **Instalar Pacotes Necessários**  
   - No console do R, instale os pacotes básicos para análise de dados:
     ```r
     install.packages(c("tidyverse", "caret", "ggplot2", "dplyr"))
     ```
   - Carregue os pacotes no seu script:
     ```r
     library(tidyverse)
     library(caret)
     library(ggplot2)
     library(dplyr)
     ```

## Variáveis do Dataset

| Variável | Descrição | Intervalo/Valores |
|----------|-----------|------------------|
| Student_ID | Identificador único para cada aluno | - |
| Idade | Idade do aluno | 18-30 anos |
| Gênero | Gênero do aluno | Masculino, Feminino, Outro |
| Study_Hours_per_Week | Horas gastas estudando por semana | 5-50 horas |
| Estilo_de_Aprendizagem_Preferido | Estilo de aprendizagem do aluno | Visual, Auditivo, Leitura/Escrita, Cinestésico |
| Cursos_online_concluídos | Número de cursos online completados | 0-20 |
| Participação_em_Discussões | Participação ativa em discussões | Sim/Não |
| Assignment_Completion_Rate | Porcentagem de tarefas concluídas | 50%-100% |
| Exam_Score | Pontuação final no exame | 40%-100% |
| Attendance_Rate | Porcentagem de presença nas aulas | 50%-100% |
| Use_of_Educational_Tech | Uso de tecnologia educacional | Sim/Não |
| Self_Reported_Stress_Level | Nível de estresse reportado | Baixo, Médio, Alto |
| Tempo_gasto_em_mídias_sociais | Horas semanais em mídias sociais | 0-30 horas |
| Sleep_Hours_per_Night | Média de horas de sono por noite | 4-10 horas |
| Final_Grade | Nota final baseada no exame | A, B, C, D, F |

## Casos de Uso

### 1. Previsão do Desempenho Acadêmico
- Análise de fatores que influenciam as notas dos exames
- Identificação de indicadores-chave de sucesso acadêmico
- Desenvolvimento de sistemas de alerta precoce para estudantes em risco

### 2. Insights Educacionais
- Compreensão do impacto dos hábitos de estudo
- Análise da efetividade de diferentes estilos de aprendizagem
- Avaliação da influência de atividades externas no desempenho

### 3. Aplicações de Machine Learning
- Desenvolvimento de modelos preditivos
- Classificação de desempenho estudantil
- Análise de correlações entre variáveis

## Como Utilizar
O dataset está disponível em formato CSV e pode ser facilmente importado usando bibliotecas como pandas (Python), dplyr (R) ou qualquer outra ferramenta de análise de dados.

## Autor
[Jan Pereira](https://github.com/janpereira82)

**Exemplo de Importação no R:**
```r
library(readr)
dataset <- read_csv("dados_estudantes.csv")
head(dataset)
```
Esse documento fornece todas as informações necessárias para começar a análise de desempenho dos estudantes com R.
