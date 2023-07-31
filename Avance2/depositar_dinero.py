#Creacion del submenu para depositar dinero
#By: Keivn Calvo

# Simulación de conversión de divisas
conversorDivisas = { #En este caso se hace uso de un diccionario llamado conversorDivisas. Las llaves en este contexto se usan par definir llaves dentro del diccionario
    "COL": 520,      # 1 dólar equivale a 520 colones
    "BTC": 0.000034  # 1 dólar equivale a 0,000034 bitcoins
}

saldoActual = 0   # Saldo inicial del usuario
intentosMax = 3   # Máximo de intentos para depositar el monto mínimo
montoMinimo = 3000  # Monto mínimo en dólares

def depositarDinero():   #Hacemos la declaracion de una funcion
    global saldoActual   #global se utiliza para indicar que la variable saldoActual se refiere a una variable definida fuera de la función, y no debe ser tratada como una variable local

    print("Divisas soportadas:")
    print("1. Colones")
    print("2. Dólares")
    print("3. Bitcoin")

    for _ in range(intentosMax):   #Hacemos un bucle para intentos de depositar dinero (3 max).
        opcionMoneda = int(input("¿En qué moneda desea depositar el dinero? "))

        if opcionMoneda not in [1, 2, 3]:   #Hacemos uso de un if pero en este caso con un cambio que es el not in
            print("Opción inválida. Intente nuevamente.")
            continue

        monedas = {1: "COL", 2: "USD", 3: "BTC"}
        monedaSeleccionada = monedas[opcionMoneda]

        montoDeposito = float(input("Ingrese el monto a depositar: "))   #Solicitamos el monto que desea el usuario depositar

        if montoDeposito <= 0:
            print("El monto debe ser un valor positivo. Intente nuevamente.")
            continue

        if monedaSeleccionada != "USD":
            tasaConversion = conversorDivisas[monedaSeleccionada]   #Utiliza la variable monedaSeleccionada como clave para acceder al valor de conversión correspondiente en el diccionario conversorDivisas
            montoDepositoUsd = montoDeposito / tasaConversion
        else:
            montoDepositoUsd = montoDeposito

        if montoDepositoUsd >= montoMinimo:   #Usamos el if para ver si el monto de deposito es igual al minimo podemos actualizar el saldo actual
            saldoActual += montoDepositoUsd
            print(f"Depósito exitoso. Saldo actual: {saldoActual:.2f} dólares.")   #El : .2f se utiliza par hacer el redondeo a dos decimales
            break   #Paramos la funcion si se cumple el if
        else:
            print(f"El monto depositado es inferior al mínimo requerido. Intento {intentosMax - _} restante(s).")

    else:
        print("Se excedió el máximo de intentos para depositar el mínimo de dinero requerido, volviendo al menú principal.")

depositarDinero()
