#Proyecto de Programación Básica

import getpass
import os


#Creacion de Funciones
#Funcion para el registro de usuario (Aun en proceso)


def registrar_usuario():
    intentos_max = 3
    file = open("deposito.txt", "r")  #Tener el valor del deposito
    monto_minimo = int(file.read())
    file.close()
    intentos = 0
    
    while intentos < intentos_max:
        usuario_id = input("Ingrese un nombre de usuario o ID: ")
        if len(usuario_id) < 5:
            print("El ID debe tener al menos cinco caracteres.")
        else:
            usuariosRegistrados = f"{usuario_id}.txt" #Revisar si ya existe unarchivo con el nombre del usuario
            if os.path.exists(usuariosRegistrados):
                print("El usuario ya está registrado")
                menu_Principal()
            else:
                nombre = input("Ingrese su nombre: ")
                pin = getpass.getpass("Ingrese su PIN (mínimo 6 dígitos): ")
                if len(pin) < 6:
                    print("El PIN debe tener al menos seis dígitos.")
                else:
                    deposito = float(input("Ingrese el monto que va a depositar: ")) #Cofirmacion deposito es suficiente
                    if deposito >= monto_minimo:
                        registroUsuario = open(usuariosRegistrados, "w") #Creacion del archivo usuario
                        registroUsuario.write("Nombre de Usuario:  " + nombre + "\n")
                        registroUsuario.write("Monto depositado:  "+str(deposito) + "\n")
                        registroUsuario.write("Pin de seguridad:  "+ pin + "\n")
                        registroUsuario.close()
                        archivoDeposito = open(usuario_id+"deposito", "w")
                        archivoDeposito.write(str(deposito))
                        archivoDeposito.close()

                        print(f"Registro exitoso. ¡Bienvenido(a) {nombre} al DreamWorld Casino!")
                        menu_Principal 
                        return
                    else:
                        print("El monto depositado es inferior al mínimo requerido. Intente nuevamente.")
                intentos += 1
                print(f"Tiene {intentos_max - intentos} intentos restantes.")

    print("Se excedió el máximo de intentos para depositar el mínimo de dinero requerido, volviendo al menú principal.")





def dreamWorldCasino():
    
    pinRegistrado = None
    intentosMaxID = 3
    intentosMaxPIN = 3
    intentosID = 0
    intentosPIN = 0
    while intentosID < intentosMaxID:
        userID= input ("Ingrese su nombre de usuario")
        usuarioRegistrado = f"{userID}.txt"
        if os.path.exists(usuarioRegistrado): #2.	Verificar que haya al menos un usuario registrado
            while intentosPIN < intentosMaxPIN:
                try:
                    archivo = open(usuarioRegistrado, "r") 
                    pinRegistrado = archivo.read() #1.	Cargar la información del usuario desde un archivo de texto
                    archivo.close()
                    solicitarPin = getpass.getpass(str("Ingrese su PIN \n"))
                    if solicitarPin in pinRegistrado:
                        print("Bienvenido")
                        submenuDreamWorld(userID)

                        return

                    else:
                        print("Pin Incorrecto, trate de nuevo")
                        intentosPIN += 1
                        if intentosPIN == intentosMaxPIN:
                            menu_Principal()
                    

                except FileNotFoundError:
                    print(f'El usuario "{userID}" no se encontró.')
                    break       

        else:
            print("Usuario no encontrado. Vuelva a intentarlo")
            intentosID += 1

        if intentosID == intentosMaxID:
            menu_Principal()




def submenuDreamWorld(autenticado):
    while True:
        print("Bienvenido al menú:")
        print("a. Retirar Dinero")
        print("b. Depositar Dinero")
        print("c. Ver saldo actual")
        print("d. Juegos en línea")
        print("e. Eliminar usuario")
        print("f. Salir")

        opcion = input("Ingresa la letra correspondiente a la opción deseada: ").lower()

        if opcion == 'a':
            retirarDinero(autenticado)
        elif opcion == 'b':
            depositarDinero(autenticado)
        elif opcion == 'c':
            verSaldoActual(autenticado)
        elif opcion == 'd':
            juegosEnLinea()
        elif opcion == 'e':
            eliminarUsuario()
        elif opcion == 'f':
            salir()
        else:
            print("Opción inválida. Por favor, ingresa una opción válida.")
    
# Simulación de conversión de divisas
conversorDivisas = { #En este caso se hace uso de un diccionario llamado conversorDivisas. Las llaves en este contexto se usan par definir llaves dentro del diccionario
    "COL": 520,      # 1 dólar equivale a 520 colones
    "BTC": 0.000034  # 1 dólar equivale a 0,000034 bitcoins
}




intentosMax = 3   # Máximo de intentos para depositar el monto mínimo
montoMinimo = 2000  # Monto mínimo en dólares

def retirarDinero(autenticado):
    global saldoActual
    intentos = 3

    try:
        deposito = open(autenticado + "deposito", "r")
        saldoActual = float(deposito.read())
        deposito.close()
    except FileNotFoundError:
        print("Archivo de depósito no encontrado. Contacte al soporte.")
        return

    while intentos > 0:
        try:
            montoRetiro = float(input("Ingrese el monto que desea retirar: "))
        except ValueError:
            print("Por favor, ingrese un monto válido (número entero).")
            continue

        if montoRetiro <= 0:
            print("El monto a retirar debe ser mayor que cero.")
            continue

        if montoRetiro > saldoActual:
            intentos -= 1
            print("Saldo insuficiente. Intentos restantes:", intentos)
            if intentos == 0:
                print("Has alcanzado el límite máximo de intentos fallidos.")
                return
        else:
            saldoActual -= montoRetiro
            print("Retiro exitoso. Saldo restante:", saldoActual)
            # Guardar el nuevo saldo en el archivo de depósito
            deposito = open(autenticado + "deposito", "w")
            deposito.write(str(saldoActual))
            deposito.close()
            return


def depositarDinero(autenticado):
    global saldoActual

    try:
        deposito = open(autenticado + "deposito", "r")
        saldoActual = float(deposito.read())
        deposito.close()
    except FileNotFoundError:
        print("Archivo de depósito no encontrado. Contacte al soporte.")
        return

    conversorDivisas = {"COL": 544, "BTC": 0.000034, "USD": 1.0}

    print("Divisas soportadas:")
    for i, (moneda, valor) in enumerate(conversorDivisas.items(), start=1):
        print(f"{i}. {moneda} (Tasa: {valor:.6f})")

    while True:
        try:
            opcionMoneda = int(input("¿En qué moneda desea depositar el dinero? "))
            if opcionMoneda in range(1, len(conversorDivisas) + 1):
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Ingrese un número válido.")

    monedas = list(conversorDivisas.keys())
    monedaSeleccionada = monedas[opcionMoneda - 1]

    montoDeposito = float(input("Ingrese el monto a depositar: "))

    if montoDeposito <= 0:
        print("El monto debe ser un valor positivo. Intente nuevamente.")
        return

    tasaConversion = conversorDivisas[monedaSeleccionada]
    montoDepositoUsd = montoDeposito / tasaConversion

    if montoDepositoUsd >= montoMinimo:
        saldoActual += montoDepositoUsd

        archivoDeposito = open(autenticado + "deposito", "w")
        archivoDeposito.write(str(saldoActual))
        archivoDeposito.close()

        print(f"Depósito exitoso. Saldo actual: {saldoActual:.2f} dólares.")
    else:
        print(f"El monto depositado es inferior al mínimo requerido.")


    # Actualizar valores de conversión en el diccionario y archivo
    conversorDivisas[monedaSeleccionada] = tasaConversion
    with open("conversor_divisas.txt", "w") as conversor_file:
        for moneda, valor in conversorDivisas.items():
            conversor_file.write(f"{moneda}:{valor}\n")




def verSaldoActual(autenticado):
    try:
        archivo = open(autenticado+"deposito", "r")
        deposito = archivo.read()
        archivo.close()
        print ("Su saldo actual es de ${}\n".format(deposito))
        submenuDreamWorld(autenticado)
    except FileNotFoundError:
        print ("Archivo no encontrado")
        submenuDreamWorld(autenticado)
 
 
 
def menuJuegos(autenticado):   #Declaracion de el menu de juegos
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
            submenuDreamWorld(autenticado)
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
    


def configuracionAvanzada():
    pinConfgAvanzada = "1234"
    pinIngresado = getpass.getpass("Ingrese el Pin Especial\n")             
    if pinIngresado == pinConfgAvanzada:                               
            print ("Configuración Avanzada\n")
            print ("Menú\n")
            print ("a. Eliminar Usuario\n")
            print ("b. Modificar Valores\n")
            print ("c. salir")
            respuesta = input("Ingrese una opción\n")
            if respuesta == "a":
                borrarUsuario()

            elif respuesta == "b":
                valoresDelSistema()

            elif respuesta == "c":
                menu_Principal()

            else:
                print ("Opción Incorrecta")
                menu_Principal()

    else:                                  #2.	Si el pin ingresado es incorrecto se devuelve al menú principal
        menu_Principal()


def borrarUsuario():
    print("Testing")


def valoresDelSistema():
    print ("Bienvenido a los Valores de sistema/n")
    print ("a. Tipo de cambio: Colones a Dolares/n")
    print ("b. Tipo de cambio: Bitcoin a Dolares/n")
    print ("c.	Valor acumulado Tragamonedas/n")
    print ("d.	Apuesta mínima Tragamonedas/n")
    print ("e.	Apuesta mínima Blackjack/n")
    print ("f.	Inversión mínima para registrarse/n")
    print ("g.	Salir/n")
    opcion = input("Seleccione la opción que quiere modificar\n")

    if opcion == "a":
        print ("a. Tipo de cambio: Colones a Dolares/n")
        #Crear archivo con tipo de cambio y poder cambiarlo
    elif opcion == "b":
        print ("b. Tipo de cambio: Bitcoin a Dolares/n")
        #Crear archivo con tipo de cambio y poder cambiarlo
    elif opcion == "c":
        print ("c.	Valor acumulado Tragamonedas/n")

    elif opcion == "d":
        print ("d.	Apuesta mínima Tragamonedas/n")

    elif opcion == "e":
        print ("e.	Apuesta mínima Blackjack/n")

    elif opcion == "f":
        deposito = str(input("Ingrese el monto minimo del Deposito\n"))
        fileDeposit = open("deposito.txt", "w")
        fileDeposit.write(deposito)
        print ("El monto del deposto fué cambiado a {} correctamente".format(deposito))
        fileDeposit.close()
        menu_Principal()

    elif opcion == "g":
        menu_Principal

    else: 
        print("Opción seleccionada no es correcta")
        valoresDelSistema()


#1.	Solicitar ID del usuario que se va a eliminar
#2.	Si el usuario existe se eliminan todos los registros asociados a ese usuario
#3.	Si no existe se muestra mensaje de error
#4.	Se devuelve al menú principal

#B)	Modificar Valores del Sistema 
#1.	Crear submenú
#a.	Tipo de cambio: Compra de dólares usando colones 
#b.	Tipo de cambio: Compra de dólares usando bitcoins
#c.	Valor acumulado Tragamonedas
#d.	Apuesta mínima Tragamonedas
#e.	Apuesta mínima Blackjack
#f.	Inversión mínima para registrarse
#g.	Salir
#2.	Preguntar cuál valor se quiere modificar
#3.	Según el valor ingresado se hace la modificación del archivo
#4.	Al seleccionar salir se devuelve al menú principal



def salir():
    print ("Prueba 4")
#1.	Se sale del programa




#---------------------------------------Programa Principal--------------------------------#

def menu_Principal():
    
    menuPrincipal = input("Seleccione una opción\na.Registro de usuario nuevo\nb.DreamWorld Casino\nc.Configuración avanzada\nd.Salir\nSu respuesta:  ")

    while True:
        
        if menuPrincipal == "a":
            registrar_usuario()
            break
        
        elif menuPrincipal == "b":
            dreamWorldCasino()
            break


        elif menuPrincipal == "c":
            configuracionAvanzada()
            break
        

        elif menuPrincipal == "d":
            print ("Gracias por visitar DreamWorld Casino")
            break

        elif menuPrincipal== "0":

            file = open("deposito.txt", "r")
            monto = int(file.read())
            file.close()
            print(monto)
            break
            
        else:
            print ("Opción no valida")
            break

print (menu_Principal())
    





































