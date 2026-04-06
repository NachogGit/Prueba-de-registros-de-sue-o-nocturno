import sqlite3
def crear_bd():
    conexion = sqlite3.connect("sueno.db")
    cursor = conexion.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            genero TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suenos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            fecha TEXT,
            hora_inicio TEXT,
            hora_fin TEXT,
            duracion_minutos INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)

    conexion.commit()
    conexion.close()
