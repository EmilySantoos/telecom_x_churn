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
