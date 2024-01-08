nombre = input("Su nombre:")
seleccion = input("Escoge entre Piedra, Papel o Tijera: \n")
spots = ["Piedra", "Papel" ,"Tijera"]
conteo = 0
conteo += 1
import random
computer_move = random.choice(spots)



def rockPaperScissors():

    if seleccion == "Piedra":
        print(computer_move)
    elif seleccion == "Papel":
        print(computer_move)
    elif seleccion == "Tijera":
        print(computer_move)


rockPaperScissors()


def winner():

    if seleccion == "Piedra" and computer_move == "Piedra" :
        print(nombre + "!!! es un Empate")
    elif seleccion == "Piedra" and computer_move == "Papel" :
        print(nombre + "!!! Perdiste :( ")
    elif seleccion == "Piedra" and computer_move == "Tijera" :
        print(nombre + "!!! Ganaste :) ")
    elif seleccion == "Tijera" and computer_move == "Tijera" :
        print(nombre + "!!! es un Empate")
    elif seleccion == "Tijera" and computer_move == "Piedra" :
        print(nombre + "!!! Perdiste :( ")
    elif seleccion == "Tijera" and computer_move == "Papel" :
        print(nombre + "!!! Ganaste :) ")
    elif seleccion == "Papel" and computer_move == "Papel" :
        print(nombre + "!!! es un Empate")
    elif seleccion == "Papel" and computer_move == "Tijera" :
        print(nombre + "!!! Perdiste :( ")
    elif seleccion == "Papel" and computer_move == "Piedra" :
        print(nombre + "!!! Ganaste :) ")
winner()
