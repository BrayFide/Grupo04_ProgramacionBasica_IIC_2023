#Creacion del registro de ususario
#Grupo4

import getpass

intentos_max = 3
monto_minimo = 1000  # Monto mínimo en dólares


#Funcion para el registro de usuario
def registrar_usuario():
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

def obtener_deposito_equivalente():   #Funcion para solicitar el deposito obligatorio con los diferentes tipos de monedas
    moneda = input("Ingrese la moneda del depósito (USD, COL, BTC): ").upper()
    if moneda == "USD":
        return float(input("Ingrese el monto en dólares: "))
    elif moneda == "COL":
        tipo_cambio_col = float(input("Ingrese el tipo de cambio: "))
        monto_col = float(input("Ingrese el monto en colones(minimo 1000 USD): "))
        return monto_col / tipo_cambio_col
    elif moneda == "BTC":
        tipo_cambio_btc = float(input("Ingrese el tipo de cambio: "))
        monto_btc = float(input("Ingrese el monto en Bitcoin(minimo 1000 USD): "))
        return monto_btc * tipo_cambio_btc
    else:
        print("Moneda no válida. Intente nuevamente.")
        return obtener_deposito_equivalente()

usuarios_registrados = {}

registrar_usuario()   # Llamar a la función de registro de usuarios
