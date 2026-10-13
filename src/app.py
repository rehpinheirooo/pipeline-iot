import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Configuração da Página do Streamlit
st.set_page_config(
    page_title="Dashboard IoT - Temperatura",
    page_icon="🌡️",
    layout="wide"
)

# Conexão com o PostgreSQL
DATABASE_URI = 'postgresql+psycopg2://postgres:sua_senha@127.0.0.1:5433/postgres'
engine = create_engine(DATABASE_URI)

# Função para carregar os dados das Views com cache
@st.cache_data
def load_data(query):
    return pd.read_sql(query, engine)

# Título do Dashboard
st.title("🌡️ Pipeline de Dados IoT: Monitoramento de Temperatura")
st.markdown("Projeto da faculdade de **Disruptive Architectures** — Visualização de dados de sensores IoT.")

# Carregar dados das Views criadas no banco
df_avg = load_data("SELECT * FROM avg_temp_por_dispositivo")
df_hora = load_data("SELECT * FROM leituras_por_hora")
df_minmax = load_data("SELECT * FROM temp_max_min_por_dia")

# Layout em colunas para os Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Média de Temperatura por Dispositivo")
    if not df_avg.empty:
        fig_avg = px.bar(df_avg, x='device_id', y='avg_temp', 
                         labels={'device_id': 'Dispositivo', 'avg_temp': 'Temp Média (°C)'},
                         color='avg_temp', color_continuous_scale='Blues')
        st.plotly_chart(fig_avg, use_container_width=True)
    else:
        st.warning("Sem dados disponíveis.")

with col2:
    st.subheader("📈 Volume de Leituras por Hora")
    if not df_hora.empty:
        fig_hora = px.line(df_hora, x='hora', y='contagem',
                           labels={'hora': 'Hora do Dia', 'contagem': 'Total de Leituras'},
                           markers=True)
        st.plotly_chart(fig_hora, use_container_width=True)
    else:
        st.warning("Sem dados disponíveis.")

# Gráfico de Linha: Máximas e Mínimas Diárias
st.subheader("📅 Temperaturas Máximas e Mínimas por Dia")
if not df_minmax.empty:
    fig_minmax = px.line(df_minmax, x='data', y=['temp_max', 'temp_min'],
                         labels={'data': 'Data', 'value': 'Temperatura (°C)', 'variable': 'Métrica'},
                         markers=True)
    st.plotly_chart(fig_minmax, use_container_width=True)
else:
    st.warning("Sem dados disponíveis.")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Renato 🚀 | Pipeline integrada com Docker, PostgreSQL, Python e Streamlit.")