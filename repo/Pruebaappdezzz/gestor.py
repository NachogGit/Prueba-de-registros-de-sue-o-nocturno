from claseusuario import Usuario
from clasecalcular import Sueno
from inserts import GestorBD
import datetime
class Gestor:
    def __init__(self):
        self.bd = GestorBD()
    # 🔹 1️⃣ Obtener o crear usuario
    def obtener_o_crear_usuario(self):
        datos_usuario = self.bd.obtener_usuario()
        if datos_usuario is None:
            print("🌙 Bienvenido")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            genero = input("Genero (m/f): ")

            usuario = Usuario(nombre, edad, genero)

            usuario_id = self.bd.insertar_usuario(
                usuario.nombre,
                usuario.edad,
                usuario.genero
            )
            print("\nUsuario creado correctamente.\n")
            return usuario, usuario_id
        else:
            usuario_id, nombre, edad, genero = datos_usuario
            usuario = Usuario(nombre, edad, genero)
            print(f"Bienvenido de nuevo, {nombre}")
            return usuario, usuario_id
    # 🔹 2️⃣ Registrar sueño
    def registrar_sueno(self, usuario, usuario_id):

        registro = Sueno(datetime.date.today())

        input("Presioná ENTER para iniciar el sueño...")
        registro.iniciar_sueno()

        input("Presioná ENTER al despertar...")
        duracion = registro.finalizar_sueno()  # devuelve minutos

        mensaje = usuario.evaluar_sueno(duracion // 60)  # pasamos horas
        print("\n📊 Evaluación del sueño:")
        print(mensaje)

        # Guardar en BD
        self.bd.insertar_sueno(
            usuario_id,
            registro.fecha,
            registro.hora_inicio.strftime("%H:%M:%S"),
            registro.hora_fin.strftime("%H:%M:%S"),
            registro.duracion_minutos
        )


    # 🔹 3️⃣ Resumen
    def resumen_sueno(self, usuario_id):

        periodo = input("1 semanal | 2 mensual: ")
        modo = input("1 tabla | 2 gráfico: ")

        if periodo == "1":
            datos = self.bd.obtener_suenos_semanales(usuario_id)
        else:
            datos = self.bd.obtener_suenos_mensuales(usuario_id)

        if modo == "1":
            self.mostrar_tabla(datos)
        else:
            self.mostrar_grafico(datos)


    # 🔹 4️⃣ Mostrar tabla
    def mostrar_tabla(self, datos):

        print("\nFecha | Duración (min)")
        print("-----------------------")

        for fecha, duracion in datos:
            print(f"{fecha} | {duracion}")


    # 🔹 5️⃣ Mostrar gráfico
    def mostrar_grafico(self, datos):

        import matplotlib.pyplot as plt

        if not datos:
            print("No hay datos para mostrar.")
            return

        fechas = [fila[0] for fila in datos]

        # Convertimos minutos a horas con 2 decimales
        duraciones = [round(fila[1] / 60, 2) for fila in datos]

        plt.figure(figsize=(10, 5))

        # 🔹 Línea negra elegante
        plt.plot(
            fechas,
            duraciones,
            color="black",
            linewidth=2
        )

        # 🔹 Buscar máximo
        max_duracion = max(duraciones)
        indice = duraciones.index(max_duracion)

        # 🔴 Punto rojo elegante (con borde negro)
        plt.scatter(
            fechas[indice],
            max_duracion,
            color="red",
            edgecolors="black",
            s=120,
            zorder=3
        )

        # 🔹 Texto discreto encima del punto
        plt.text(
            fechas[indice],
            max_duracion + 0.1,
            f"{max_duracion} h",
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

        # 🎨 Estética minimalista
        plt.title("Resumen de Sueño", fontsize=14, fontweight="bold")
        plt.ylabel("Horas dormidas")
        plt.xticks(rotation=45)

        plt.grid(alpha=0.2)  # grilla suave
        plt.tight_layout()

        plt.show()