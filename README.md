# 🌡️ Pipeline de Dados IoT: Monitoramento de Temperatura

> **Projeto Acadêmico** — Desenvolvido para a disciplina de **Arquiteturas Disruptivas**.

Este projeto implementa um pipeline de dados *end-to-end* (de ponta a ponta) para ingestão, armazenamento, transformação e visualização de dados de sensores IoT de temperatura.

---

## 🏗️ Arquitetura da Solução

O fluxo do pipeline é composto pelas seguintes etapas:
1. **Ingestão (ETL)**: Leitura de dados brutos a partir de um arquivo CSV utilizando **Python** (`Pandas` e `SQLAlchemy`).
2. **Armazenamento**: Inativação e carregamento dos dados em um banco relacional **PostgreSQL** rodando isoladamente em um contêiner **Docker**.
3. **Modelagem e Transformação (SQL)**: Criação de Views otimizadas no banco para agregações e tratamento de datas.
4. **Visualização (Dashboard)**: Interface interativa construída com **Streamlit** e gráficos dinâmicos em **Plotly**.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.14+
- **Banco de Dados**: PostgreSQL (via Docker)
- **Bibliotecas Python**: Pandas, SQLAlchemy, Psycopg2, Streamlit, Plotly
- **Contêineres**: Docker & Docker Compose
- **Ambiente de Desenvolvimento**: VS Code

---

## 📂 Estrutura do Projeto

```text
pipeline-iot/
│
├── data/
│   └── IOT-temp.csv           # Dataset bruto de sensores IoT
│
├── src/
│   ├── app.py                 # Código do Dashboard Streamlit
│   ├── etl.py                 # Script de extração, transformação e carga
│   ├── create_views.py        # Script Python para criação das Views SQL
│   └── views.sql              # Consultas SQL para modelagem analítica
│
├── venv/                      # Ambiente virtual Python
└── README.md                  # Documentação do Projeto

🚀 Como Executar o Projeto
Siga os passos abaixo para configurar e rodar o projeto em sua máquina local:

1. Clonar o Repositório / Abrir a Pasta
Abra a pasta do projeto no seu editor de código (ex: VS Code).

2. Subir o Banco de Dados no Docker
Certifique-se de que o Docker Desktop está aberto e execute o comando no terminal para iniciar o contêiner PostgreSQL (mapeando para a porta 5433 para evitar conflitos locais):

DOS
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5433:5432 -d postgres

3. Ativar o Ambiente Virtual e Instalar Dependências
No Prompt de Comando (CMD) ou PowerShell:

DOS
python -m venv venv
venv\Scripts\activate
pip install pandas sqlalchemy psycopg2-binary streamlit plotly

4. Executar o Pipeline ETL (Ingestão de Dados)
Execute o script para popular o banco de dados com as leituras do CSV:

DOS
python src/etl.py

5. Criar as Views Analíticas no Banco
Execute o script de modelagem SQL:

DOS
python src/create_views.py

6. Iniciar o Dashboard Interativo (Streamlit)
Por fim, abra a interface web de visualização:

DOS
streamlit run src/app.py

O sistema abrirá automaticamente uma aba no seu navegador padrão em http://localhost:8501.

📊 Principais Métricas e Gráficos do Dashboard
Média de Temperatura por Dispositivo: Gráfico de barras comparando o desempenho térmico de cada sensor IoT.

Volume de Leituras por Hora: Análise temporal da frequência de dados coletados ao longo do dia.

Temperaturas Máximas e Mínimas Diárias: Acompanhamento de flutuações extremas de temperatura por dia.

👨‍💻 Autor
Desenvolvido por Renato como parte do projeto acadêmico de Arquiteturas Disruptivas.