from sqlalchemy import Column, Integer, String, Float
from config.database import Base
from pydantic import BaseModel
from typing import List

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    minutos_jugados = Column(Integer)
    goles = Column(Integer)
    disparos_a_puerta = Column(Integer)
    disparos_fuera = Column(Integer)
    faltas_recibidas = Column(Integer)
    faltas_cometidas = Column(Integer)
    tarjetas_amarillas = Column(Integer)
    tarjetas_rojas = Column(Integer)
    pases_completados = Column(Integer)
    total_pases = Column(Integer)
    paradas_realizadas = Column(Integer)
    distancia_recorrida_km = Column(Float)
    velocidad_maxima_km_h = Column(Float)
    partidos_jugados = Column(Integer)
    recuperaciones = Column(Integer)
    
class JugadorMinutos(BaseModel):
    jugador: str
    minutos_jugados: int
