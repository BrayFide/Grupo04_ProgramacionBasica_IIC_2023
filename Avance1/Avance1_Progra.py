#Proyecto de Programación Básica


usuarios_registrados = "brayton"

def registro_usuario_nuevo():
    print("------ Registro de Usuario Nuevo ------")
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su nombre de usuario o ID: ")
        if len(usuario) < 5:
            print("El ID debe tener al menos cinco caracteres.")
            intentos += 1
        elif usuario in usuarios_registrados:
            print("El ID ingresado ya está registrado.")
            intentos += 1
        else:
            nombre = input("Ingrese su nombre: ")
            pin = input("Ingrese su PIN (6 dígitos): ")
            if len(pin) != 6:
                print("El PIN debe tener exactamente 6 dígitos.")
            else:
                confirmacion_pin = input("Ingrese nuevamente su PIN: ")
                if pin != confirmacion_pin:
                    print("El PIN no coincide.")
                else:
                    print("Registro exitoso.")
                    return
    print("Se excedió el máximo de intentos para ingresar un ID válido.")



opcion = input("1. Registro de usuario nuevo\n")



while True:
    
        if opcion == "1":
            registro_usuario_nuevo()
        elif opcion == "2":
            dreamworld_casino()
        elif opcion == "3":
            configuracion_avanzada()
        elif opcion == "4":
            salir = True
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
