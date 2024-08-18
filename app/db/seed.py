from sqlalchemy.orm import Session
from models.jugador import Jugador

def insertar_datos_iniciales(db: Session):
    data = {
        "jugador": ["Unai Simón", "Carvajal", "Le Normand", "Nacho", "Rodri", "Mikel Merino", "Fabián Ruiz", "Zubimendi", "Lamine Yamal", "Laporte", "Dani Olmo", "Morata", "Oyarzabal", "Cucurella", "Nico Williams", "Raya", "Vivian", "Joselu", "Ferran", "Grimaldo", "Jesus Navas", "Baena", "Fermin", "Remmiro"],
        "minutos_jugados": [570, 471, 443, 262, 521, 178, 542, 140, 507, 411, 431, 454, 197, 546, 494, 90, 122, 89, 152, 114, 157, 25, 28, 0],
        "goles": [0, 1, 0, 0, 1, 1, 2, 0, 1, 0, 3, 1, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        "disparos_a_puerta": [0, 2, 0, 0, 1, 2, 5, 0, 7, 1, 6, 4, 3, 1, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        "disparos_fuera": [0, 0, 0, 0, 2, 1, 7, 0, 7, 3, 4, 6, 2, 0, 4, 0, 1, 3, 4, 0, 0, 0, 0, 0],
        "faltas_recibidas": [0, 3, 3, 3, 7, 1, 4, 1, 6, 5, 7, 9, 2, 12, 2, 0, 1, 1, 2, 0, 1, 0, 1, 0],
        "faltas_cometidas": [0, 5, 8, 0, 7, 9, 4, 4, 7, 2, 2, 12, 3, 9, 9, 0, 1, 1, 4, 0, 2, 1, 1, 0],
        "tarjetas_amarillas": [0, 3, 2, 0, 3, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        "tarjetas_rojas": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "pases_completados": [189, 266, 325, 121, 411, 105, 381, 106, 161, 452, 147, 78, 56, 300, 180, 36, 103, 15, 32, 81, 45, 10, 9, 0],
        "total_pases": [237, 290, 341, 128, 439, 124, 422, 112, 196, 480, 174, 105, 59, 323, 198, 39, 109, 18, 39, 85, 52, 11, 10, 0],
        "paradas_realizadas": [14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
        "distancia_recorrida_km": [34.9, 53.97, 49.77, 27.75, 68.52, 28.09, 69.11, 20.04, 55.32, 56.09, 50.28, 52.92, 25.49, 63.1, 54.53, 5.92, 14.69, 10.8, 19.99, 15.03, 18.58, 4.5, 3.92, 0],
        "velocidad_maxima_km_h": [28.5, 32.5, 31.3, 31.9, 33, 31.4, 32.6, 29.4, 33.3, 33, 30.5, 32, 32.1, 33.1, 35.8, 27.4, 30.2, 29.6, 36, 31.2, 33, 31.3, 32.5, 0],
        "partidos_jugados": [6, 5, 6, 4, 6, 7, 6, 4, 7, 6, 6, 7, 7, 6, 6, 1, 2, 2, 5, 2, 3, 2, 1, 0],
        "recuperaciones": [0, 31, 27, 8, 0, 10, 0, 12, 0, 37, 11, 5, 2, 34, 6, 0, 11, 2, 0, 10, 5, 2, 0, 0]
    }

    if db.query(Jugador).count() == 0:  # Verifica si la tabla ya tiene datos
        jugadores = [
            Jugador(
                nombre=data["jugador"][i],
                minutos_jugados=data["minutos_jugados"][i],
                goles=data["goles"][i],
                disparos_a_puerta=data["disparos_a_puerta"][i],
                disparos_fuera=data["disparos_fuera"][i],
                faltas_recibidas=data["faltas_recibidas"][i],
                faltas_cometidas=data["faltas_cometidas"][i],
                tarjetas_amarillas=data["tarjetas_amarillas"][i],
                tarjetas_rojas=data["tarjetas_rojas"][i],
                pases_completados=data["pases_completados"][i],
                total_pases=data["total_pases"][i],
                paradas_realizadas=data["paradas_realizadas"][i],
                distancia_recorrida_km=data["distancia_recorrida_km"][i],
                velocidad_maxima_km_h=data["velocidad_maxima_km_h"][i],
                partidos_jugados=data["partidos_jugados"][i],
                recuperaciones=data["recuperaciones"][i]
            )
            for i in range(len(data["jugador"]))
        ]

        db.add_all(jugadores)
        db.commit()
