import pandas as pd
import os

# Criar pastas
os.makedirs("data/processed", exist_ok=True)

# Ler dados brutos
df = pd.read_json("data/raw/telecom_churn_raw.json", lines=True)

# Limpeza de dados
df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# Salvar dados limpos
df.to_csv("data/processed/telecom_churn_clean.csv", index=False)
print("✅ Dados processados salvos em data/processed/telecom_churn_clean.csv")
