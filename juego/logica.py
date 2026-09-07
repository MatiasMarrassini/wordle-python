import random
import time
import math
from datos import obtener_palabras

def calcular_tiempo_total(tiempo_inicial) -> tuple:
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    # Se usa la libreria math para redondear para abajo los minutos (Evita calcular 1 minuto extra)
    minutos = math.floor(tiempo_total / 60)
    segundos = round(tiempo_total % 60)

    return minutos, segundos

def conseguir_palabra(dificultad, usadas: list[str]) -> list:
    """
    Esta funcion devuelve una palabra aleatoria tomando como parametro la cantidad de caracteres (5-7) y las palabras usadas anteriormente 
    """
    
    # restar utilizadas utilizando sets
    arr = set(obtener_palabras(dificultad)) - set(usadas)
    # reconvertir a lista
    arr = list(arr)
    # seleccionar palabra aleatoriamente
    palabra = arr[random.randint(0, len(arr) - 1)].upper()
    # sacar el salto de linea
    palabra = palabra.replace("\n","")
    return palabra

def acomodar_jugadores(jugadores: list[dict]) -> list:
    """
    la funcion devuelve una lista con los jugadores ordenados de mayor total de primeros turnos a menor, para evitar que no toque siempre el mismo jugador como primero
    """

    # Crear una copia de la lista para no modificar la original
    jugadores_ordenados = jugadores.copy()
    
    # Algoritmo de ordenamiento burbuja
    n = len(jugadores_ordenados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if jugadores_ordenados[j]["total_primeros_turnos"] < jugadores_ordenados[j + 1]["total_primeros_turnos"]:
                # Intercambiar elementos
                jugadores_ordenados[j], jugadores_ordenados[j + 1] = jugadores_ordenados[j + 1], jugadores_ordenados[j]
    
    return jugadores_ordenados
