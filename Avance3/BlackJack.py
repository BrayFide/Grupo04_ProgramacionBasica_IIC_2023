#Desarrollo de estructura par el juego blackjack
import os
import random
def blackjack(autenticado):
    try: 
        archivo = open(autenticado+"deposito", "r")
        contDeposito = archivo.read()
        archivo.close()
        depositoUsuario = float(contDeposito)

    except FileNotFoundError:
        print ("Archivo no encontrado")
        submenuDreamWorld(autenticado)    


    if os.path.exists("apuestaMinima.txt"):
        print("Instrucciones")
        fileapuesta = open("apuestaMinima.txt", "r")
        contApuesta = fileapuesta.read()
        fileapuesta.close()
        apuestaMinima = float(contApuesta)
        apuestaInicial = float(input("Ingrese el monto que quiere apostar"))
    else: 
        fileapuesta = open("apuestaMinima.txt", "w")
        fileapuesta.write("25")
        fileapuesta.close()
        fileapuesta = open("apuestaMinima.txt", "r")
        contApuesta = fileapuesta.read()
        fileapuesta.close()
        apuestaMinima = float(contApuesta)
        
        print("Instrucciones")
        apuestaInicial = float(input("Ingrese el monto que quiere apostar"))

    while True:
            if depositoUsuario > apuestaMinima:
                print ("Repartiendo cartas")
                elejirCarta()

                break

        


            elif depositoUsuario < apuestaMinima:
                print("saldo Insuficiente, usted tiene ${}, y ocupa como minimo ${} para poder jugar, haga un deposito en su cuenta".format(depositoUsuario , apuestaMinima))
                submenuDreamWorld(autenticado)
                break

def elejirCarta():
    
    valorCartas = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    tipoNaipe = ["Trebol", "Diamante", "Corazones", "Espadas"]

    for _ in range(1):
        resultadoUno = random.choice(valorCartas)
        resultadoDos = random.choice(tipoNaipe)
    

    if resultadoUno == 11:
        valorCarta = "J"
    elif resultadoUno == 12:
        valorCarta = "Q"
    elif resultadoUno == 13:
        valorCarta = "K"
    else:
        valorCarta = resultadoUno
    
    if resultadoDos in ["Diamante", "Corazones"]:
    
        print("\033[91mCarta {} de {}\033[0m".format(valorCarta, resultadoDos))
    else:
        # Imprime en color normal
        print("Carta {} de {}".format(valorCarta, resultadoDos))

    return (valorCarta, resultadoDos)
    
def elejirCartaOculta():
    
    valorCartas = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    tipoNaipe = ["Trebol", "Diamante", "Corazones", "Espadas"]

    resultadoUno = random.choice(valorCartas)
    resultadoDos = random.choice(tipoNaipe)
    return (resultadoUno, resultadoDos)

def repartirCartas():
    usuario = []
    crupier = []

    for i in range(2):

        print("Usuario:")
        usuario.append(elejirCarta())

        print("Crupier:")
        if i == 0:
            crupier.append(elejirCarta())
        else:
            crupier.append(elejirCartaOculta())
            print("Carta Oculta")


    print (usuario)
    print (crupier)

repartirCartas()




