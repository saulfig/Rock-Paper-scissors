nombre = input("Su nombre:")
seleccion = input("Escoge entre Piedra, Papel o Tijera: \n")
spots = ["Piedra", "Papel" ,"Tijera"]
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
    global puntosSeleccion 
    puntosSeleccion = 0
    if seleccion == "Piedra" and computer_move == "Piedra" :
        puntosSeleccion = 0
        print(nombre + "!!! es un Empate")
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Piedra" and computer_move == "Papel" :
        print(nombre + "!!! Perdiste :( ")
        puntosSeleccion = 0
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Piedra" and computer_move == "Tijera" :
        print(nombre + "!!! Ganaste :) ")
        puntosSeleccion +=1
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Tijera" and computer_move == "Tijera" :
        print(nombre + "!!! es un Empate")
        puntosSeleccion = 0
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Tijera" and computer_move == "Piedra" :
        print(nombre + "!!! Perdiste :( ")
        puntosSeleccion = 0
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Tijera" and computer_move == "Papel" :
        print(nombre + "!!! Ganaste :) ")
        puntosSeleccion +=1
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Papel" and computer_move == "Papel" :
        print(nombre + "!!! es un Empate")
        puntosSeleccion = 0
        print("Puntos:" , puntosSeleccion)
    elif seleccion == "Papel" and computer_move == "Tijera" :
        print(nombre + "!!! Perdiste :( ")
        puntosSeleccion = 0
        print("Puntos:" + puntosSeleccion)
    elif seleccion == "Papel" and computer_move == "Piedra" :
        print(nombre + "!!! Ganaste :) ")
        puntosSeleccion +=1
        print("Puntos:" + puntosSeleccion)
winner()
