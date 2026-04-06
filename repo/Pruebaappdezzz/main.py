from gestor import Gestor


def main():

    gestor = Gestor()

    usuario, usuario_id = gestor.obtener_o_crear_usuario()

    opcion = input("1 registrar sueño | 2 ver resumen: ")

    if opcion == "1":
        gestor.registrar_sueno(usuario, usuario_id)

    elif opcion == "2":
        gestor.resumen_sueno(usuario_id)


if __name__ == "__main__":
    main()