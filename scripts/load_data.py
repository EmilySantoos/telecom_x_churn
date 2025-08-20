import pandas as pd

# Carregar dados tratados
df = pd.read_csv("data/processed/telecom_churn_clean.csv")
print("Dados carregados com sucesso!")
print(df.head())
