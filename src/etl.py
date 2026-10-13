import pandas as pd
from sqlalchemy import create_engine

# Alterado de 5432 para 5433 para evitar conflitos no Windows
DATABASE_URI = 'postgresql+psycopg2://postgres:sua_senha@127.0.0.1:5433/postgres'
engine = create_engine(DATABASE_URI)

# Ler o arquivo CSV
csv_path = 'data/IOT-temp.csv'
print(f"Lendo dados de {csv_path}...")
df = pd.read_csv(csv_path)

# Limpar e padronizar o nome das colunas
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Inserir os dados na tabela 'temperature_readings'
print("Enviando dados para o banco PostgreSQL...")
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso no PostgreSQL!")