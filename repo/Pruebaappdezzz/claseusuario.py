

class Usuario:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def horas_recomendadas(self):
        horas_min = None
        horas_max = None
        categoria = None

        if self.edad < 1:
            categoria = "Bebe"
            hora_min = 14
            hora_max = 17

        elif self.edad <= 4:
            categoria = "Niño pequeño"
            hora_min = 11
            hora_max = 14

        elif self.edad <= 12:
            categoria = "Niño"
            hora_min = 9
            hora_max = 12

        elif self.edad <= 17:
            categoria = "Adolescente"
            hora_min = 8
            hora_max = 10

        elif self.edad <= 64:
            categoria = "Adulto"
            hora_min = 7
            hora_max = 10

        return categoria,hora_min, hora_max
    def evaluar_sueno(self, duracion):
        categoria, hora_min, hora_max = self.horas_recomendadas()

        if duracion < hora_min:
            return f"Dormiste poco. Deberías dormir entre {hora_min} y {hora_max} horas."
        elif hora_min <= duracion <= hora_max:
            return f"Buen ciclo nocturno. Dormiste lo recomendado ({hora_min}-{hora_max} horas)."
        else:
            return f"Dormiste de más. Lo recomendado es entre {hora_min} y {hora_max} horas."