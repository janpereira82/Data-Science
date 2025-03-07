# Análise de Desempenho dos Estudantes
# Bibliotecas necessárias para análise
library(tidyverse)  # Conjunto de pacotes para manipulação e visualização de dados
library(caret)      # Ferramentas para classificação e regressão
library(corrplot)   # Visualização de matrizes de correlação
library(randomForest) # Implementação do algoritmo Random Forest
library(ggplot2)    # Sistema para criação de gráficos

# Carregar e preparar os dados
# Leitura do arquivo CSV contendo informações dos estudantes
data <- read.csv('student_performance_large.csv')

# Exploração inicial dos dados
# Exibe a estrutura do dataset (tipos de variáveis e primeiras observações)
str(data)
# Apresenta estatísticas resumidas de todas as variáveis
summary(data)

# Pré-processamento: Conversão de variáveis categóricas para fatores
# Isso é necessário para análises estatísticas e visualizações adequadas
data$Gender <- as.factor(data$Gender)  # Gênero como fator
data$Preferred_Learning_Style <- as.factor(data$Preferred_Learning_Style)  # Estilo de aprendizagem
data$Participation_in_Discussions <- as.factor(data$Participation_in_Discussions)  # Participação
data$Use_of_Educational_Tech <- as.factor(data$Use_of_Educational_Tech)  # Uso de tecnologia
data$Self_Reported_Stress_Level <- as.factor(data$Self_Reported_Stress_Level)  # Nível de estresse
data$Final_Grade <- as.factor(data$Final_Grade)  # Nota final

# Análise Exploratória de Dados (EDA)

# 1. Distribuição das Notas Finais
# Criação de gráfico de barras para visualizar a distribuição das notas
grade_dist <- ggplot(data, aes(x = Final_Grade, fill = Final_Grade)) +
  geom_bar() +  # Usa barras para representar frequências
  scale_fill_brewer(palette = "Set2") +  # Paleta de cores harmoniosa
  theme_minimal() +  # Tema minimalista para melhor visualização
  theme(legend.position = "none",  # Remove legenda redundante
        plot.title = element_text(size = 14, face = "bold"),
        axis.title = element_text(size = 12)) +
  labs(title = "Distribuição das Notas Finais dos Estudantes",
       subtitle = "Análise da Frequência de Cada Nota",
       x = "Nota Final",
       y = "Número de Estudantes")

# 2. Análise da Relação entre Horas de Estudo e Desempenho
# Gráfico de dispersão com linha de tendência
study_exam <- ggplot(data, aes(x = Study_Hours_per_Week, y = Exam_Score)) +
  geom_point(aes(color = Final_Grade), alpha = 0.6) +  # Pontos com transparência
  geom_smooth(method = "lm", se = TRUE, color = "darkblue") +  # Linha de regressão com intervalo de confiança
  scale_color_brewer(palette = "Set1") +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, face = "bold"),
        axis.title = element_text(size = 12),
        legend.title = element_text(size = 10),
        legend.position = "right") +
  labs(title = "Relação entre Horas de Estudo e Desempenho no Exame",
       subtitle = "Com Linha de Tendência Linear",
       x = "Horas de Estudo por Semana",
       y = "Nota do Exame (%)",
       color = "Nota Final")

# 3. Análise de Desempenho por Estilo de Aprendizagem
# Boxplot para comparar distribuições de notas entre diferentes estilos
learning_style_perf <- ggplot(data, aes(x = Preferred_Learning_Style, y = Exam_Score, fill = Preferred_Learning_Style)) +
  geom_boxplot() +  # Boxplot para mostrar distribuição
  scale_fill_brewer(palette = "Pastel1") +  # Cores suaves
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),  # Rótulos em ângulo para melhor legibilidade
        plot.title = element_text(size = 14, face = "bold"),
        axis.title = element_text(size = 12),
        legend.position = "none") +
  labs(title = "Desempenho no Exame por Estilo de Aprendizagem",
       subtitle = "Distribuição das Notas por Cada Estilo",
       x = "Estilo de Aprendizagem Preferido",
       y = "Nota do Exame (%)")

# 4. Análise de Correlação entre Variáveis Numéricas
# Seleciona apenas variáveis numéricas e calcula correlações
numeric_vars <- data %>%
  select_if(is.numeric)  # Filtra apenas variáveis numéricas
corr_matrix <- cor(numeric_vars)  # Calcula matriz de correlação

# 5. Análise do Impacto do Nível de Estresse
# Combinação de violin plot e boxplot para análise detalhada
stress_impact <- ggplot(data, aes(x = Self_Reported_Stress_Level, y = Exam_Score, fill = Self_Reported_Stress_Level)) +
  geom_violin(alpha = 0.7) +  # Violin plot para densidade
  geom_boxplot(width = 0.2, alpha = 0.7) +  # Boxplot sobreposto
  scale_fill_brewer(palette = "RdYlBu") +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, face = "bold"),
        axis.title = element_text(size = 12),
        legend.position = "none") +
  labs(title = "Impacto do Nível de Estresse no Desempenho do Exame",
       subtitle = "Combinação de Violin Plot e Box Plot",
       x = "Nível de Estresse",
       y = "Nota do Exame (%)")

# 6. Análise de Desempenho por Gênero
# Boxplot para comparar distribuições de notas entre gêneros
gender_performance <- ggplot(data, aes(x = Gender, y = Exam_Score, fill = Gender)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3") +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, face = "bold"),
        axis.title = element_text(size = 12),
        legend.position = "none") +
  labs(title = "Desempenho no Exame por Gênero",
       subtitle = "Distribuição das Notas por Gênero",
       x = "Gênero",
       y = "Nota do Exame (%)")

# Configuração para salvar múltiplos gráficos em um único PDF
pdf("analysis_plots.pdf", width = 10, height = 8)

# Define layout para múltiplos gráficos por página
par(mfrow = c(2, 2), mar = c(4, 4, 2, 2))

# Imprime gráficos em ordem lógica
print(grade_dist)
print(study_exam)
print(learning_style_perf)
corrplot(corr_matrix, 
         method = "color",
         type = "upper",
         addCoef.col = "black",
         tl.col = "black",
         tl.srt = 45,
         diag = FALSE,
         title = "Matriz de Correlação das Variáveis Numéricas")
print(stress_impact)
print(gender_performance)

# Restaura configurações padrão do dispositivo gráfico
par(mfrow = c(1, 1))
dev.off()

# Modelagem Preditiva usando Random Forest

# Seleção de características (features) para o modelo
# Inclui variáveis numéricas relevantes para previsão
features <- c("Age", "Study_Hours_per_Week", "Online_Courses_Completed",
             "Assignment_Completion_Rate", "Exam_Score", "Attendance_Rate",
             "Time_Spent_on_Social_Media", "Sleep_Hours_per_Night")

# Limpeza de nomes de colunas
# Remove caracteres especiais dos nomes das colunas
colnames(data) <- gsub(" \\(%\\)", "", colnames(data))
colnames(data) <- gsub(" \\(hours/week\\)", "", colnames(data))

# Divisão dos dados em conjuntos de treino (80%) e teste (20%)
set.seed(123)  # Define semente para reprodutibilidade
trainIndex <- createDataPartition(data$Final_Grade, p = 0.8, list = FALSE)
train_data <- data[trainIndex, ]
test_data <- data[-trainIndex, ]

# Treinamento do modelo Random Forest
# Utiliza 100 árvores de decisão para classificação
rf_model <- randomForest(Final_Grade ~ .,
                        data = train_data[, c(features, "Final_Grade")],
                        ntree = 100)

# Realiza previsões no conjunto de teste
predictions <- predict(rf_model, test_data)

# Avaliação do desempenho do modelo
# Gera matriz de confusão e métricas de avaliação
confusion_matrix <- confusionMatrix(predictions, test_data$Final_Grade)

# Visualiza importância das variáveis no modelo
varImpPlot(rf_model)

# Imprime resultados da avaliação do modelo
print("Desempenho do Modelo:")
print(confusion_matrix)

# Salva gráficos finais em PDF
pdf("analysis_plots.pdf")
print(grade_dist)
print(study_exam)
print(learning_style_perf)
corrplot(corr_matrix, method = "color")
print(stress_impact)
dev.off()