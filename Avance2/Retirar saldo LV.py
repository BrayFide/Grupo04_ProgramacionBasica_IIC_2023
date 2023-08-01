saldo_actual = 1000

def retirar_dinero():
    global saldo_actual
    intentos = 3

    while intentos > 0:
        try:
            monto_retiro = int(input("Ingrese el monto que desea retirar: "))
        except ValueError:
            print("Por favor, ingrese un monto válido (número entero).")
            continue

        if monto_retiro <= 0:
            print("El monto a retirar debe ser mayor que cero.")
            continue

        if monto_retiro > saldo_actual:
            intentos -= 1
            print("Saldo insuficiente. Intentos restantes:", intentos)
            if intentos == 0:
                print("Has alcanzado el límite maximo de intentos fallidos.")
                return
        else:
            saldo_actual -= monto_retiro
            print("Retiro exitoso. Saldo restante:", saldo_actual)
            return

def depositar_dinero():
    global saldo_actual
    try:
        monto_deposito = int(input("Ingrese el monto que desea depositar: "))
    except ValueError:
        print("Por favor, ingrese un monto válido (número entero).")
        return

    if monto_deposito <= 0:
        print("El monto a depositar debe ser mayor que cero.")
        return

    saldo_actual += monto_deposito
    print("Depósito exitoso. Saldo actual:", saldo_actual)

def ver_saldo_actual():
    print("Saldo actual:", saldo_actual,"$")

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
        retirar_dinero()
    elif opcion == 'b':
        depositar_dinero()
    elif opcion == 'c':
        ver_saldo_actual()
    elif opcion == 'd':
        juegos_en_linea()
    elif opcion == 'e':
        eliminar_usuario()
    elif opcion == 'f':
        salir()
    else:
        print("Opción inválida. Por favor, ingresa una opción válida.")
