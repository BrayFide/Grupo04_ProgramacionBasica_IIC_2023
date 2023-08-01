#Proyecto de Programación Básica



#Creacion de Funciones

def registro_usuario():
    print ("Prueba 1")

#1.	Registro de usuario
#a.	Si el Usuario elige la función "Registro de usuario nuevo" : Se deben cumplir las siguientes condiciones para registrar el nombre de usuario:
#b.	El nombre usuario debe ser mayor o igual a 5 caracteres: 
#c.	Si el N.U es menor a 5 caracteres se imprime un error y el mensaje "El Nombre de usuario debe ser mayor a 5 caracteres". 
#d.	El nombre de usuario no debe estar previamente registrado (Estructura del Sistema de Archivos y biblioteca os)
#e.	Si se genera una alerta el usuario tiene 3 intentos para agregar la información correcta, al fallar los 3 intentos vuelve al menú inicio.


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
    print ("Prueba 3")


#1.	Solicitud de PIN especial
#2.	Si el pin ingresado es incorrecto se devuelve al menú principal
#3.	El PIN especial no debe ser mostrado en la pantalla
#4.	Si el PIN es correcto desplegar submenú
#a.	Eliminar Usuario
#b.	Modificar Valores
#c.	Salir




#A)	Eliminar usuario

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

menuPrincipal = input("Seleccione una opción\na.Registro de usuario nuevo\nb.DreamWorld Casino\nc.Configuración avanzada\nd.Salir\nSu respuesta:  ")

while True:
    
    if menuPrincipal == "a":
        registro_usuario()
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



    





































