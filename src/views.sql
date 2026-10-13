-- View 1: Média de temperatura por dispositivo
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT id as device_id, AVG(out_in) as avg_temp
FROM temperature_readings
GROUP BY id;

-- View 2: Contagem de leituras por hora do dia
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT DATE_TRUNC('hour', date::timestamp) as hora, COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- View 3: Temperaturas máximas e mínimas por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT DATE(date::timestamp) as data, MAX(out_in) as temp_max, MIN(out_in) as temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;