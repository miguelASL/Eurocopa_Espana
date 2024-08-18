from models.jugador import Seleccion as SeleccionModel
from schemas.seleccion import Seleccion

class SeleccionService():

    def __init__(self, db) -> None:
        self.db = db
        
    def get_all_jugadores(self):
        result = self.db.query(SeleccionModel).all()
        return result
    
    def get_jugador_by_id(self, id: int):
        result = self.db.query(SeleccionModel).filter(SeleccionModel.id == id).first()
        return result
    
    def get_jugadores_by_nombre(self, nombre: str):
        result = self.db.query(SeleccionModel).filter(SeleccionModel.jugador.ilike(f"%{nombre}%")).all()
        return result
    
    def get_top_goleadores(self, limit: int = 3):
        result = self.db.query(SeleccionModel).order_by(SeleccionModel.goles.desc()).limit(limit).all()
        return result
    
    def get_jugadores_con_mas_minutos(self, limit: int = 3):
        result = self.db.query(SeleccionModel).order_by(SeleccionModel.minutos_jugados.desc()).limit(limit).all()
        return result
    
    def get_jugador_con_mas_recuperaciones(self):
        result = self.db.query(SeleccionModel).order_by(SeleccionModel.recuperaciones.desc()).first()
        return result
