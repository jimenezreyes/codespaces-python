#Juego de piedra papel o tijera

import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntuacion = {"jugador": 0, "oponente": 0}

    while True:
        oponente = random.choice(opciones)
        jugador = input("Elige piedra, papel o tijeras: ").lower()

        if jugador not in opciones:
            print("Opción no válida. Por favor, elige piedra, papel o tijeras.")
            continue

        print(f"Tu oponente eligió {oponente}")

        if jugador == oponente:
            print("¡Es un empate!")
        elif (
            (jugador == "piedra" and oponente == "tijeras")
            or (jugador == "tijeras" and oponente == "papel")
            or (jugador == "papel" and oponente == "piedra")
        ):
            print("¡Ganaste esta ronda!")
            puntuacion["jugador"] += 1
        else:
            print("¡Perdiste esta ronda!")
            puntuacion["oponente"] += 1

        print(f"Puntuación - Jugador: {puntuacion['jugador']}, Oponente: {puntuacion['oponente']}")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_de_nuevo != "sí":
            break

    print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_piedra_papel_tijeras()
