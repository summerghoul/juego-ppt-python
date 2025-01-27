
partidas_max = 3
cant_partidas = 0
fin_del_juego = False

print("¡Bienvenidos al juego de piedra papel o tijera!")

nombre_1 = input("ingresar el nombre del jugador 1: ")
nombre_2 = input("ingresar el nombre del jugador 2: ")

txt = " ,que eliges? piedra, papel o tijera: "

tirada_jugador_1 = nombre_1 + txt
tirada_jugador_2 = nombre_2 + txt

while not fin_del_juego:

    if not cant_partidas < partidas_max:
        print("¡Fin del juego!")
        break


    # primera partida
    jugador_1 = input(tirada_jugador_1).lower()
    # segunda partida
    jugador_2 = input(tirada_jugador_2).lower()


    situacion_1 = jugador_1 == "piedra" and jugador_2 == "tijera"
    situacion_2 = jugador_1 == "papel" and jugador_2 == "piedra"
    situacion_3 = jugador_1 == "tijera" and jugador_2 == "papel"

    if jugador_1 == jugador_2:
        print("¡EMPATEEE!")
    elif situacion_1 or situacion_2 or situacion_3:
        print("¡Felicidades!", nombre_1, "haz ganado esta partida")
    else:
        print("¡Felicidades!", nombre_2, "haz ganado esta partida")

    cant_partidas += 1
    
