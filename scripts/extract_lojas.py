import pandas as pd
import os

# Criar pasta "lojas" se não existir
os.makedirs("data/lojas", exist_ok=True)

# Links Raw dos CSVs
urls = {
    "loja1": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/main/data/loja1.csv",
    "loja2": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/main/data/loja2.csv",
    "loja3": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/main/data/loja3.csv"
}

# Baixar e salvar cada CSV
for nome, url in urls.items():
    df = pd.read_csv(url)
    df.to_csv(f"data/lojas/{nome}.csv", index=False)
    print(f"✅ {nome}.csv salvo em data/lojas/")
