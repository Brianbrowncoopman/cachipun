import random


def jugar():
    usuario = input("Escoge una opcion: 'piedra' para piedra, 'papel' para papel , 'tijera' para tijera. \n").lower()
    computadora = random.choice(['piedra', 'papel', 'tijera'])

    if usuario == computadora:
        return '¡empate!'
    
    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def gano_el_jugador(jugador, oponente):
    # retornar true si gana el jugador
    # jugador = piedra y oponente = tijera (piedra>tijera)
    #tijera gana a papel(tijera>papel)
    #papel gana a piedra(papel>piedra)
    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False
    

print(jugar())