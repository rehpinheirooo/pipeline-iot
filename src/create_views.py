from sqlalchemy import create_engine, text

# Conexão com o banco na porta 5433
DATABASE_URI = 'postgresql+psycopg2://postgres:sua_senha@127.0.0.1:5433/postgres'
engine = create_engine(DATABASE_URI)

# Comandos SQL com DROP VIEW para evitar conflitos de tipo de dados
sql_commands = """
DROP VIEW IF EXISTS avg_temp_por_dispositivo CASCADE;
DROP VIEW IF EXISTS leituras_por_hora CASCADE;
DROP VIEW IF EXISTS temp_max_min_por_dia CASCADE;

CREATE VIEW avg_temp_por_dispositivo AS
SELECT id as device_id, AVG(temp) as avg_temp
FROM temperature_readings
GROUP BY id;

CREATE VIEW leituras_por_hora AS
SELECT DATE_TRUNC('hour', TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) as hora, COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) as data, MAX(temp) as temp_max, MIN(temp) as temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;
"""

# Executando no banco
with engine.begin() as conn:
    for statement in sql_commands.split(';'):
        if statement.strip():
            conn.execute(text(statement))

print("As Views foram limpas e recriadas com sucesso!")