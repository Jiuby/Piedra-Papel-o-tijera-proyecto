import random

opciones = ("piedra", "papel", "tijera")

computer_wins = 0
yo_wins = 0
rondas = 1


while True:

    print("^" *10)
    print("Ronda", rondas)
    print("^" *10)

    print("puntos computador", computer_wins)
    print("puntos propios", yo_wins)



    usuario = input("piedra, papel o tijera: ")
    usuario = (usuario.lower())

    rondas += 1


    if usuario not in opciones:
        print("que putas, eso no es valido")
        continue



    computadora = random.choice(opciones)  #importamos random para que eliga algo random de opciones

    print(f"User option: {usuario}")
    print(f"Computer option: {computadora}")


    print()
    if usuario == computadora:
        print("empate")
    elif usuario == "piedra": #  si el usuario digita esto se comienza a cumplir lo de abajo
        #estas son las condiciones del computador

        if computadora == "tijera":
            print("piedra gana a tijera")
            print("gano el usuario")
            yo_wins += 1

        else:
            print("papel gana a piedra")
            print("gano la computadora")
            computer_wins +=1

    elif usuario == "papel":
        if computadora == "piedra":
            print("papel gana a piedra")
            print("gano el usuario")
            yo_wins += 1

        else:
            print("tijera gana a papel")
            print("gano el computador")
            computer_wins +=1

    elif usuario == "tijera":
        if computadora == "papel":
            print("tijera gana a papel")
            print("gano el usuario")
            yo_wins += 1

        else:
            print("piedra gana a tijera")
        print("gano el computador")
        computer_wins += 1


    if computer_wins == 2:
        print("gano la computadora")
        break

    if yo_wins == 2:
        print("gano el humano")
        break

