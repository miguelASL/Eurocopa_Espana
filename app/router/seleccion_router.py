from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session as DBSession
from sqlalchemy import text
from config.database import Session, engine
from sqlalchemy.engine.row import Row
from typing import List
from models.jugador import JugadorMinutos

seleccion_router = APIRouter()

def row_to_dict(row):
    if isinstance(row, Row):
        return row._asdict()
    return {column: value for column, value in row.items()}

# Obtener todos los jugadores
@seleccion_router.get("/seleccion", response_description="Obtener todos los jugadores")
def get_seleccion():
    with Session() as db:
        seleccion = db.execute(text("SELECT * FROM jugadores")).fetchall()
        if not seleccion:
            raise HTTPException(status_code=404, detail="No se encontraron los jugadores")
        return [row_to_dict(row) for row in seleccion]

# Obtener jugador por 'ID'
@seleccion_router.get("/seleccion/jugador/{id}", response_description="Obtener jugador por 'ID'")
def get_seleccion_by_id(id: int):
    with Session() as db:
        seleccion = db.execute(text("SELECT * FROM jugadores" 
                                    "WHERE id = :id"), {'id': id}).fetchone()
        if seleccion is None:
            raise HTTPException(status_code=404, detail="Jugador no encontrado")
        return row_to_dict(seleccion)

# Máximo goleador
@seleccion_router.get("/seleccion/goleador/{nombre}", response_description="Obtener máximo goleador de la seleccion española de futbol")
def get_max_goleador(nombre: str):
    with Session() as db:
        max_goleador = db.execute(text(
            "SELECT nombre, goles FROM jugadores "
            "WHERE LOWER(nombre) LIKE LOWER(:name) "
            "ORDER BY goles DESC"
        ), {'name': f"%{nombre}%"}).fetchone()
        
        if max_goleador is None:
            raise HTTPException(status_code=404, detail="No se encontró el máximo goleador")
        return row_to_dict(max_goleador)

# Minutos jugados de los jugadores
@seleccion_router.get("/seleccion/top-minutos/{nombre}", response_description="Obtener los minutos jugados de los jugadores")
def get_top_minutos(nombre: str):
    with Session() as db:
        top_minutos = db.execute(text(
            "SELECT nombre, minutos_jugados FROM jugadores "
            "WHERE LOWER(nombre) LIKE LOWER(:name) "
            "ORDER BY minutos_jugados DESC"
        ), {'name': f"%{nombre}%"}).fetchall()
        
        if not top_minutos:
            raise HTTPException(status_code=404, detail="No se encontraron jugadores")
        return [row_to_dict(row) for row in top_minutos]
        
# Total de goles marcados por el equipo
@seleccion_router.get("/seleccion/total-goles", response_description="Obtener total de goles marcados por el equipo")
def get_total_goles():
    with Session() as db:
        total_goles = db.execute(text("SELECT SUM(goles) as total_goles FROM jugadores")).fetchone()
        if total_goles is None or total_goles[0] is None:
            raise HTTPException(status_code=404, detail="No se encontraron goles")
        return {"total_goles": total_goles[0]}

# Distancia promedio recorrida por los jugadores
@seleccion_router.get("/seleccion/distancia-promedio/{nombre}", response_description="Get promedio distancia recorrida by jugadores")
def get_distancia_promedio(nombre: str):
    with Session() as db:
        distancia_promedio = db.execute(text(
            "SELECT AVG(distancia_recorrida_km) as distancia_promedio "
            "FROM jugadores "
            "WHERE LOWER(nombre) = LOWER(:nombre)"
        ), {'nombre': nombre}).fetchone()
        
        if distancia_promedio is None or distancia_promedio[0] is None:
            raise HTTPException(status_code=404, detail="No se encontró distancia promedio")
        
        return {"distancia_promedio": distancia_promedio[0]}
    
# Velocidad máxima promedio de los jugadores
@seleccion_router.get("/seleccion/velocidad-promedio/{nombre}", response_description="Get promedio velocidad máxima by jugadores")
def get_velocidad_promedio(nombre: str):
    with Session() as db:
        velocidad_promedio = db.execute(text(
            "SELECT AVG(velocidad_maxima_km_h) as velocidad_promedio "
            "FROM jugadores "
            "WHERE LOWER(nombre) = LOWER(:nombre)"
        ), {'nombre': nombre}).fetchone()
        
        if velocidad_promedio is None or velocidad_promedio[0] is None:
            raise HTTPException(status_code=404, detail="No se encontró velocidad promedio")
        
        return {"velocidad_promedio": velocidad_promedio[0]}
