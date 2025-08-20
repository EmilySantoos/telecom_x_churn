import pandas as pd
import requests
import os

# Criar pastas
os.makedirs("data/raw", exist_ok=True)

# URL do JSON
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science/main/TelecomX_Data.json"

# Baixar dados
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_json("data/raw/telecom_churn_raw.json", orient="records", lines=True)
    print("✅ Dados brutos salvos em data/raw/telecom_churn_raw.json")
else:
    print(f"❌ Erro ao acessar a API: {response.status_code}")


# Criar pasta de dados processados e plots
os.makedirs("data/processed", exist_ok=True)
os.makedirs("data/plots", exist_ok=True)

# Limpeza de dados
df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# Salvar CSV limpo
df.to_csv("data/processed/telecom_churn_clean.csv", index=False)
print("✅ Dados processados salvos em data/processed/telecom_churn_clean.csv")

# Análise exploratória (EDA)
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df)
plt.title("Distribuição de Churn")
plt.savefig("data/plots/churn_distribution.png")
plt.show()

