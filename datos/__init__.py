import json
import os

PATH_USUARIOS = os.path.join(os.path.dirname(__file__), "Usuarios.json")
PATH_PALABRAS = os.path.join(os.path.dirname(__file__), "palabras")
PATH_CONFIGURACION = os.path.join(os.path.dirname(__file__), "config.json")


def registrar_datos_partida(datos_partida: dict) -> None:
    """
    Registra los datos de una partida en el archivo de usarios.json
   """
    usuarios = obtener_usuarios()  # usuarios del json

    for jugador in datos_partida["jugadores"]:  # se repite maximo 2 veces
        # Creo que los puntos mejor calcularlos aparte
        if  datos_partida["ganador"] != None and jugador["id"] == datos_partida["ganador"]["id"]:
            jugador["puntaje"] += calcular_puntos_ganados(jugador["intentos"])
        else:
            jugador["puntaje"] -= 0

        for usuario in usuarios:
            if usuario["id"] == jugador["id"]:
                usuario["total_partidas"] = jugador["total_partidas"]
                usuario["puntaje"] = jugador["puntaje"]
                usuario["total_primeros_turnos"] = jugador["total_primeros_turnos"]
                usuario["palabras_usadas"].append(datos_partida["palabra"])
                # palabras usadas es una lista
                # palabra es un str

        with open(PATH_USUARIOS, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=2, ensure_ascii=False)


def guardar_nuevo_usuario(datos_usuario: dict) -> None:
    with open(PATH_USUARIOS, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    usuarios.append(datos_usuario)
    with open(PATH_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=2, ensure_ascii=False)


def obtener_usuarios():
    with open(PATH_USUARIOS, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    return usuarios


def obtener_palabras(longitud: int) -> list[str]:
    assert longitud in range(5, 8)
    with open(os.path.join(PATH_PALABRAS, f"{longitud}.txt"), encoding="utf-8") as f:
        palabras = f.readlines()

    palabras = list(map(lambda x: x.replace("\n", ""), palabras))

    return palabras


def calcular_puntos_ganados(arriesgos: int) -> int:
    puntos = [50, 40, 30, 20, 10]

    return puntos[arriesgos]

def guardar_configuracion(config: dict) -> None:
    with open(PATH_CONFIGURACION, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def cargar_configuracion() -> dict:
    with open(PATH_CONFIGURACION, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config

# TESTEO
if __name__ == "__main__":
    print(cargar_configuracion())
