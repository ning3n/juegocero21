import os, random
os.system('cls')

def juego():
    cartas = 10
    totalDeCartas = 10
    while cartas > 0 or cartas < 21:
        while totalDeCartas != 0:
            opciones = [-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9]
            cantidadCartas=[1,2]
            cartaAElegir1 = random.choice(opciones)
            cartaAElegir2 = random.choice(opciones)
            cantidadAElegir = random.choice(cantidadCartas)
            if cantidadAElegir == 1:
                print("Se operara con la carta: ", cartaAElegir1)
                cartas+=cartaAElegir1
                totalDeCartas=totalDeCartas-1
                print(cartas)
            elif cantidadAElegir == 2:
                print("Las cartas a elegir son: ", cartaAElegir1, " y ", cartaAElegir2)
                eleccion = int(input("Elige una de las cartas: "))
                print(cartas)
                if eleccion == cartaAElegir1:
                    cartas += cartaAElegir1
                    print(cartas)
                else:
                    cartas += cartaAElegir2
                    print(cartas)
                totalDeCartas = totalDeCartas - 2
            print(cartas)

            if cartas <= 0 or cartas >= 21:
                print("Perdiste!") 
                exit()        

        if cartas <= 0 or cartas >= 21:
            print("Perdiste!")
            exit()
        else:
            print("Ganaste!")
            exit()


nuevojuego = input("1-Nuevo Juego  2-Salir\n")

if nuevojuego=="1" or nuevojuego=="Nuevo Juego":
    juego()
else:
    exit()
    os.system('cls')