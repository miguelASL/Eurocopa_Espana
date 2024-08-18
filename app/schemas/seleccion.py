from pydantic import BaseModel, Field
from typing import Optional

# Schema
class Seleccion(BaseModel):
    id: Optional[int] = None
    jugador: str
    minutos_jugados: int
    goles: int
    disparos_a_puerta: int
    disparos_fuera: int
    faltas_recibidas: int
    faltas_cometidas: int
    tarjetas_amarillas: int
    tarjetas_rojas: int
    pases_completados: int
    total_pases: int
    paradas_realizadas: int
    distancia_recorrida_km: float
    velocidad_maxima_km_h: float
    partidos_jugados: int
    recuperaciones: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "jugador": "Unai Simón",
                "minutos_jugados": 570,
                "goles": 0,
                "disparos_a_puerta": 0,
                "disparos_fuera": 0,
                "faltas_recibidas": 0,
                "faltas_cometidas": 0,
                "tarjetas_amarillas": 0,
                "tarjetas_rojas": 0,
                "pases_completados": 189,
                "total_pases": 237,
                "paradas_realizadas": 14,
                "distancia_recorrida_km": 34.9,
                "velocidad_maxima_km_h": 28.5,
                "partidos_jugados": 6,
                "recuperaciones": 0
            },
            "example_2": {
                "id": 2,
                "jugador": "Carvajal",
                "minutos_jugados": 471,
                "goles": 1,
                "disparos_a_puerta": 2,
                "disparos_fuera": 0,
                "faltas_recibidas": 3,
                "faltas_cometidas": 5,
                "tarjetas_amarillas": 3,
                "tarjetas_rojas": 1,
                "pases_completados": 266,
                "total_pases": 290,
                "paradas_realizadas": 0,
                "distancia_recorrida_km": 53.97,
                "velocidad_maxima_km_h": 32.5,
                "partidos_jugados": 5,
                "recuperaciones": 31
            }
        }
