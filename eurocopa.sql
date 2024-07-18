-- Ver todos los datos de la tabla
SELECT * FROM seleccion.seleccion;

--  Distribución de minutos jugados
SELECT jugador, minutos_jugados
FROM seleccion
ORDER BY minutos_jugados DESC;

-- Relación entre minutos jugados y goles
SELECT jugador, goles
FROM seleccion
WHERE goles > 0;

-- Comparación de pases acertados, fallados y totales
SELECT jugador, pases_acertados, (total_de_pases - pases_acertados) AS pases_fallados, total_de_pases
FROM seleccion;

-- Analisis Avanzado
SELECT jugador, goles, minutos_jugados, 
       (goles / minutos_jugados) * 100 AS goles_por_minuto
FROM seleccion
WHERE minutos_jugados > 0 and goles > 0
ORDER BY goles_por_minuto DESC;

-- Analisis descriptivo 
SELECT 
    AVG(minutos_jugados) AS promedio_minutos,
    AVG(goles) AS promedio_goles,
    AVG(disparos_a_puerta) AS promedio_disparos_a_puerta,
    AVG(disparos_fuera) AS promedio_disparos_fuera,
    AVG(faltas_recibidas) AS promedio_faltas_recibidas,
    AVG(faltas_cometidas) AS promedio_faltas_cometidas,
    AVG(tarjetas_amarillas) AS promedio_tarjetas_amarillas,
    AVG(tarjetas_rojas) AS promedio_tarjetas_rojas,
    AVG(pases_acertados) AS promedio_pases_acertados,
    AVG(paradas_realizadas) AS promedio_paradas_realizadas,
    AVG(distancia_recorrida_km) AS promedio_distancia_recorrida_km,
    AVG(velocidad_maxima_km_h) AS promedio_velocidad_maxima_km_h,
    AVG(partidos_jugados) AS promedio_partidos_jugados,
    AVG(recuperaciones) AS promedio_recuperaciones
FROM seleccion;
