def main():
    balance = 0  # Saldo inicial en dólares
    tasasDeCambio = {
        "colones": 0.0017,  # Valor de 1 colón en dólares
        "bitcoin": 26755   # Valor de 1 bitcoin en dólares
    }
    intentosMaximos = 3  # Número máximo de intentos

    for intento in range(1, intentosMaximos + 1):
        print(f"\nIntento {intento} de {intentosMaximos}")
        print("\nDivisas soportadas:")
        print("1. Colones")
        print("2. Dólares")
        print("3. Bitcoin")
        option = input("¿En qué moneda desea depositar el dinero? ")

        if option == "1":
            currency = "colones"
        elif option == "2":
            currency = "dólares"
        elif option == "3":
            currency = "bitcoin"
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
            continue


        monto = float(input(f"Ingrese el monto en {currency}: "))
        
        if currency != "dólares":
            tasaDeCambio = tasasDeCambio[currency]
            montoEquivalente = monto * tasaDeCambio
        else:
            montoEquivalente = monto
        
        if montoEquivalente < 3000:
            print("El monto debe ser al menos de 3000 dólares o su equivalente.")
            if intento == intentosMaximos:
                print("Límite de intentos alcanzado. Gracias por usar nuestro sistema.")
                break
            continue

        balance += montoEquivalente
        print("Transacción realizada de forma correcta.")
        print(f"Saldo actual: {balance:.2f} dólares")

        subMenu = input("\n¿Desea realizar otra transacción? (s/n): ")
        if subMenu.lower() != "s":
            break

    print("¡Gracias por usar nuestro sistema de depósitos!")

main()