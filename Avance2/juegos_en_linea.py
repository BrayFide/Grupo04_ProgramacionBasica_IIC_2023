#Menu de Juegos en linea (Blackjack y Tragamonedas)

def menuJuegos():   #Declaracion de el menu de juegos
    while True:      #Usamos un while true para la eleccion de el juego
        print("------ Juegos en línea ------")
        print("1. Blackjack")
        print("2. Tragamonedas")
        print("3. Salir")

        opcionJuego = input("Seleccione un juego (1-3): ")   #Solicitamos que juego desea jugar

        if opcionJuego == "1":   #Hacemos uso del if para la esta estructura de desicion
            jugarBlackjack()
        elif opcionJuego == "2":
            jugarTragamonedas()
        elif opcionJuego == "3":
            print("Gracias por jugar. ¡Hasta luego!")   #Usamos el print para que la persona elija salir del menu
            break
        else:
            print("Opción inválida. Intente nuevamente.")   #Este print se presenta cuando el usuario no haga una eleccion correcta

def jugarBlackjack():
    # Codigo para el juego de Blackjack
    print("Jugando Blackjack...")
    # Aquí va la lógica del juego

def jugarTragamonedas():
    # Codigo para el juego de Tragamonedas
    print("Jugando Tragamonedas...")
    # Aquí va la lógica del juego

menuJuegos()