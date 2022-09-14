import random

opciones=["piedra","fuego","tijera","humano","esponja","papel","aire","agua","pistola"]
comp=random.randint(0,8)

fin="continuar"
while fin != "fin":
    fin=str(input("Ingresa fin si quieres terminar de jugar o para seguir escribir continuar" ))
    jug=input(print(f"ESCOJE " ,opciones, " "))
    print("Eleccion computadora " , opciones[comp]," ")

    if jug==comp:
        print("Empate")

    elif jug=="piedra":
        if comp=="fuego":
            print("ganaste")
        elif comp=="tijera":
            print("ganaste")
        elif comp=="humano":
            print("ganaste")
        elif comp=="esponja":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="fuego":
        if comp=="tijera":
            print("ganaste")
        elif comp=="humano":
            print("ganaste")
        elif comp=="esponja":
            print("ganaste")
        elif comp=="papel":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="tijera":
        if comp=="humano":
            print("ganaste")
        elif comp=="esponja":
            print("ganaste")
        elif comp=="papel":
            print("ganaste")
        elif comp=="aire":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="humano":
        if comp=="esponja":
            print("ganaste")
        elif comp=="papel":
            print("ganaste")
        elif comp=="aire":
            print("ganaste")
        elif comp=="agua":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="esponja":
        if comp=="papel":
            print("ganaste")
        elif comp=="aire":
            print("ganaste")
        elif comp=="agua":
            print("ganaste")
        elif comp=="pistola":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="papel":
        if comp=="aire":
            print("ganaste")
        elif comp=="agua":
            print("ganaste")
        elif comp=="pistola":
            print("ganaste")
        elif comp=="roca":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="aire":
        if comp=="agua":
            print("ganaste")
        elif comp=="pistola":
            print("ganaste")
        elif comp=="roca":
            print("ganaste")
        elif comp=="fuego":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="agua":
        if comp=="pistola":
            print("ganaste")
        elif comp=="roca":
            print("ganaste")
        elif comp=="fuego":
            print("ganaste")
        elif comp=="tijera":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="pistola":
        if comp=="roca":
            print("ganaste")
        elif comp=="fuego":
            print("ganaste")
        elif comp=="tijera":
            print("ganaste")
        elif comp=="humano":
            print("ganaste")
        else:
            print("perdiste")
    elif jug=="roca":
        if comp=="fuego":
            print("ganaste")
        elif comp=="tijera":
            print("ganaste")
        elif comp=="humano":
            print("ganaste")
        elif comp=="esponja":
            print("ganaste")
        else:
            print("perdiste")
    else:
        print("ingresa una opción valida")