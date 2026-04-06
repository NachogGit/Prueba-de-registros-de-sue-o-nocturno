import datetime as horita


class Sueno:
    def __init__(self, fecha ):
        self.fecha = fecha
        self.hora_inicio = None
        self.hora_fin = None
    

    def iniciar_sueno(self):
        self.hora_inicio = horita.datetime.now()
        print(f"El sueño comenzó a las: {self.hora_inicio.strftime('%H:%M:%S')}")
        return self.hora_inicio
    

    def finalizar_sueno(self):
        if self.hora_inicio is None:
            print("⚠️ No hay un sueño iniciado.")
            return
     

        self.hora_fin = horita.datetime.now()

        duracion = self.hora_fin - self.hora_inicio
        self.duracion_minutos = duracion.seconds // 60

        horas = self.duracion_minutos // 60
        minutos = self.duracion_minutos % 60

        print(f"El sueño finalizó a las: {self.hora_fin.strftime('%H:%M:%S')}")
        print(f"Total dormido: {horas} horas y {minutos} minutos")

        return self.duracion_minutos

