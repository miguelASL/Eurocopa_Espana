import sqlite3 as sql

def create_db():
    conn = sql.connect("seleccion.db")
    conn.commit()
    conn.close()

def create_table():
    conn = sql.connect("seleccion.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS seleccion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jugador TEXT,
        minutos_jugados INTEGER,
        goles INTEGER,
        asistencias INTEGER,
        disparos_a_puerta INTEGER,
        disparos_fuera INTEGER,
        faltas_recibidas INTEGER,
        faltas_cometidas INTEGER,
        tarjetas_amarillas INTEGER,
        tarjetas_rojas INTEGER,
        pases_acertados INTEGER,
        pases_fallados INTEGER,
        paradas_realizadas INTEGER
    )"""
    )
    conn.commit()
    conn.close()
    
def insert_data(jugador, minutos_jugados, goles, asistencias, disparos_a_puerta, faltas_recibidas, faltas_cometidas, tarjetas_amarillas, tarjetas_rojas, pases_completados, pases_fallados, paradas_realizadas):
    conn = sql.connect("seleccion.db")
    cursor = conn.cursor()
    instruccion = """
    INSERT INTO seleccion (jugador, minutos_jugados, goles, asistencias, disparos_a_puerta, faltas_recibidas, faltas_cometidas, tarjetas_amarillas, tarjetas_rojas, pases_completados, pases_fallados, paradas_realizadas)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    valores = (jugador, minutos_jugados, goles, asistencias, disparos_a_puerta, faltas_recibidas, faltas_cometidas, tarjetas_amarillas, tarjetas_rojas, pases_completados, pases_fallados, paradas_realizadas)
    cursor.execute(instruccion, valores)
    conn.commit()
    conn.close()
    
def readRows():
    conn = sql.connect("seleccion.db")
    cursor = conn.cursor()
    instruccion = "SELECT * FROM seleccion"
    cursor.execute(instruccion)
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    
def insertRows(seleccionList):
    conn = sql.connect("seleccion.db")
    cursor = conn.cursor()
    instruccion = """
    INSERT INTO seleccion (jugador, minutos_jugados, goles, asistencias, disparos_a_puerta, faltas_recibidas, faltas_cometidas, tarjetas_amarillas, tarjetas_rojas, pases_acertados, pases_fallados, paradas_realizadas)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(instruccion, seleccionList)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # create_db()
    # create_table()
    # insert_data()
    # readRows()
    seleccionList=[]
    # insertRows(seleccionList)