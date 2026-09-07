import time
import juego.logica as logica
import UI


def partida(jugadores: list[dict], dificultad: int) -> dict:
    """
    Esta funcion se encarga de efectuar una partida, cuando la misma finaliza devuelve los datos de los resultados
    """

    # Variables de la partida
    jugadores = logica.acomodar_jugadores(jugadores)
    palabras_usadas = [palabra_usada for j in jugadores for palabra_usada in j["palabras_usadas"]]
    palabra_adivinar = logica.conseguir_palabra(dificultad, palabras_usadas)
    arriesgos = []  # palabras arriesgadas
    letras_adivinadas = ["_" for _ in range(dificultad)]  # letras adivinadas
    tiempo_inicial = time.time()
    partida_terminada = False
    arriesgo = ""
    turno = 0
    ganador = None
    shows = []
    
    # crear key intentos:0 para contabilizar individualmente los arriesgos de cada jugador
    for jugador in jugadores:
        jugador["intentos"] = 0

    # ejecución de la partida
    while not partida_terminada:
        jugador = jugadores[turno]
        arriesgo, letras_adivinadas = UI.ronda(palabra_adivinar, dificultad, jugador, letras_adivinadas, arriesgos, shows)
        arriesgos.append(arriesgo)
        jugador["intentos"] += 1

        # chequear si alguien ganó
        if arriesgo == palabra_adivinar:
            partida_terminada = True
            ganador = jugador
        # chequear si se acabaron los intentos
        elif len(arriesgos) >= 5:
            partida_terminada = True
        else:
            # la partida continua
            turno = (turno + 1) % len(jugadores)

    #sumar al total de partidas jugadas
    for jugador in jugadores:
        jugador["total_partidas"] += 1

    datos_partida = {
        "tiempo_total": logica.calcular_tiempo_total(tiempo_inicial),
        "ganador": ganador,
        "jugadores": jugadores,
        "arriesgos": arriesgos,
        "letras_adivinadas": letras_adivinadas,
        "palabra": palabra_adivinar
    }

    return datos_partida

'''
if __name__ == "__main__":
    partida([{
    "id": 1,
    "usuario": "juan",
    "contrasena": "password123",
    "puntaje": 120,
    "total_partidas": 0,
    "total_primeros_turnos": 0,
    "palabras_usadas": ["perro"]
    }],5)

'''