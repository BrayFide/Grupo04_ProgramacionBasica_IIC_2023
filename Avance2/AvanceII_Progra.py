#Proyecto de Programación Básica

import getpass
import os


#Creacion de Funciones
#Funcion para el registro de usuario
def registrar_usuario():
    intentos_max = 3
    monto_minimo =  1000
    intentos = 0
    while intentos < intentos_max:  #Estructura WHILE con estructura de desicion para identificar el numero de intentos
        usuario_id = input("Ingrese un nombre de usuario o ID: ")   #Se le solicita al usuario el ID
        if len(usuario_id) < 5:
            print("El ID debe tener al menos cinco caracteres.")
        elif usuario_id in usuarios_registrados:
            print("El ID ingresado ya está registrado.")
        else:
            nombre = input("Ingrese su nombre: ")   #Solicitud de nombre
            pin = getpass.getpass("Ingrese su PIN (mínimo 6 dígitos): ")   #Solicitar al usuario el pin y utilizar la biblioteca "getpass"
            if len(pin) < 6:
                print("El PIN debe tener al menos seis dígitos.")
            else:
                deposito = obtener_deposito_equivalente()
                if deposito >= monto_minimo:
                    usuarios_registrados[usuario_id] = {
                        "nombre": nombre,
                        "pin": pin,
                        "saldo": deposito
                    }
                    print(f"Registro exitoso. ¡Bienvenido(a) {nombre} al DreamWorld Casino!")
                    return
                else:
                    print("El monto depositado es inferior al mínimo requerido. Intente nuevamente.")
        intentos += 1
        print(f"Tiene {intentos_max - intentos} intentos restantes.")

    print("Se excedió el máximo de intentos para depositar el mínimo de dinero requerido, volviendo al menú principal.")
#2.	Solicitar el nombre

#3.	Creación de PIN:
#a.	Solicitar al usuario un numero de máximo 6 dígitos, este pin no debe ser visible al usuario, y se puede ingresar las veces necesarias hasta que sea válido.
#b.	Volver a solicitar el PIN al usuario para autenticarlo. 
#c.	Mostrar mensaje si no son iguales

#4.	Proceso de depósito:
#a.	 Obtener el monto mínimo de depósito del archivo de configuración avanzada.
#b.	Solicitar al usuario que realice un depósito en la moneda deseada (dólares, colones o bitcoin).
#c.	Realizar conversión de la moneda si es diferente a dólar
#d.	Verificar si el depósito cumple con el mínimo requerido:
#e.	Si el depósito es menor al mínimo, mostrar un mensaje de error
#f.	Registrar el depósito en la cuenta asociada al usuario.
#g.	Dar al usuario hasta tres intentos para depositar el monto mínimo
#h.	Si consume los tres intentos, mostrar un mensaje de alerta y volver al menú principal.

#5.	Guardar la información del nuevo usuario y generar el sistema de carpetas y archivos asociados: 
#a.	Utilizar la biblioteca os para crear directorios y archivos.
#b.	Guardar la información del usuario en los archivos correspondientes.
#c.	Mostrar un mensaje de éxito y regresar al menú principal.

#6.	(Investigar Sistema de carpetas y archivos)

#7.	Regresa al menú principal


def dreamWorldCasino():
    print ("Prueba 2")
#1.	Cargar la información del usuario desde un archivo de texto
#2.	Verificar que haya al menos un usuario registrado
#3.	Autenticar al usuario:
#a.	Solicitar ID
#b.	Verificar que sea valido y que esté registrado
#c.	Si es invalido
#d.	Se da 3 intentos para ingresar un ID valido
#e.	Si falla los 3 intentos vuelve al menú principal y se imprime un mensaje de error
#f.	Si es valido
#g.	Solicitar PIN
#h.	Se da 3 intentos para ingresar PIN valido
#i.	Si el PIN es invalido después de los 3 intentos se imprime mensaje de error
#j.	Se devuelve al menú principal
#k.	El PIN no debe ser visible

#4.	Usuario Autenticado
#a.	Imprimir mensaje de bienvenida
#b.	Cagar toda la información del usuario desde archivos de texto



#4.1	Submenú
#1-	Crear funciones para el submenú
#a.	Retirar Dinero
#b.	Depositar Dinero
#c.	Ver saldo actual
#d.	Juegos en línea
#e.	Eliminar usuario
#f.	Salir

#A-	Retirar dinero
#1.	Imprimir saldo actual en la pantalla
#2.	Preguntar cuánto dinero desea retirar
#3.	Si el monto es mayor al saldo
#a.	Imprimir mensaje de error
#b.	Evitar transacción
#c.	Después de 3 intentos fallidos se devuelve al menú principal
#d.	Actualizar saldos de cada cuenta con el valor actual
#4.	Si el monto es menor al saldo
#a.	Se resta el monto del saldo
#b.	Imprimir mensaje de confirmación de retiro
#c.	Imprimir saldo actual
#d.	Se regresa al Submenú

#B-	Depositar Dinero
#1.	Imprimir lista de divisas aceptadas
#2.	Solicitar que tipo de divisa se va a usar
#3.	Solicitar el monto a depositar
#4.	Verificar que el monto sea positivo
#5.	Imprimir mensaje de error si monto es negativo 
#6.	Guardar valores para la conversión de divisas en un archivo
#a.	Hacer conversión de colones a dólares
#b.	Hacer conversión de bitcoins a dólares
#c.	Agregar monto si se usan dólares
#7.	Imprimir mensaje de confirmación de la transacción
#8.	Imprimir el saldo actual
#9.	Regresar al submenú

#C-	Ver Saldo Actual
#1.	Se imprime saldo actual en dólares
#2.	Se regresa al submenú

#D-	Juegos en línea
#1.	Crear submenú con dos juegos
#a.	Blackjack
#b.	Tragamonedas
#c.	Salir
#2.	Preguntar a usuario que elija una opción

#A.	Blackjack
#1.	Mostrar instrucciones del juego



#B.	Tragamonedas





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
<<<<<<< HEAD
        print ("El monto del deposto fué cambiado a {} correctamente".format(deposito))
        fileDeposit.close()
        menu_Principal()
=======
        print ("El monto del deposto fué cambiado a {} correctamente".format deposito)
        fileDeposit.close()
>>>>>>> a16b79a194b13e752778a45744c681877b212763

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
        
        else:
            print ("Opción no valida")
            break

print (menu_Principal())
    





































