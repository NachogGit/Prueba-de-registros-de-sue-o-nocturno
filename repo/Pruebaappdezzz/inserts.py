from datetime import datetime
import sqlite3

class GestorBD:
    def __init__(self, nombre_bd="sueno.db"):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def insertar_usuario(self, nombre, edad, genero):
        self.cursor.execute("""
            INSERT INTO usuarios (nombre, edad, genero)
            VALUES (?, ?, ?)
        """, (nombre, edad, genero))
        self.conexion.commit()

    def obtener_usuario(self):
        self.cursor.execute("""
            SELECT id, nombre, edad, genero FROM usuarios LIMIT 1
        """)
        return self.cursor.fetchone()

      

    def insertar_sueno(self, usuario_id, fecha, hora_inicio, hora_fin, duracion_minutos):
        self.cursor.execute("""
            INSERT INTO suenos (
                usuario_id,
                fecha,
                hora_inicio,
                hora_fin,
                duracion_minutos
            )
            VALUES (?, ?, ?, ?, ?)
        """, (usuario_id, fecha, hora_inicio, hora_fin, duracion_minutos))
        self.conexion.commit()
    def obtener_suenos_semanales(self, usuario_id):
        import datetime
        hoy = datetime.date.today()
        hace_7_dias = hoy - datetime.timedelta(days=7)

        self.cursor.execute("""
            SELECT fecha, duracion_minutos
            FROM suenos
            WHERE usuario_id = ?
            AND fecha >= ?
            ORDER BY fecha
        """, (usuario_id, hace_7_dias))

        return self.cursor.fetchall()
        # SELECT con filtro de fecha

    def obtener_suenos_mensuales(self, usuario_id):
        import datetime
        hoy = datetime.date.today()
        hace_30_dias = hoy - datetime.timedelta(days=30)

        self.cursor.execute("""
            SELECT fecha, duracion_minutos
            FROM suenos
            WHERE usuario_id = ?
            AND fecha >= ?
            ORDER BY fecha
        """, (usuario_id, hace_30_dias))

        return self.cursor.fetchall()

    def cerrar(self):
        self.conexion.close()
