"""
Funciones relacionadas con la interaccion del usuario
"""
import os


import juego
from UI.decorador_procedimientos import procedimiento
import UI.logica
import UI.login
from UI.ranking import ranking
from utils import cambiar_color, obtener_color
import UI.alinear


def seleccionarDificultad() -> int:
    print("╔══════════════════════════════╗")
    print("║   Seleccion de Dificultad    ║")
    print("╠══════════════════════════════╣")
    print("║    1. Facil (5 letras)       ║")
    print("║    2. Normal (6 letras)      ║")
    print("║    3. Dificil (7 letras)     ║")
    print("╚══════════════════════════════╝")
    selec = input("Seleccione una dificultad (1-3):")
    while selec not in ["1", "2", "3"]:
        selec = input("Seleccione una dificultad (1-3):")


    return int(selec)+4


def menu(usuarios:list[dict], dificultad:int) -> dict:
    usuarios = [u["usuario"] for u in usuarios]
    usuarios = " || ".join(usuarios)

    if len(usuarios) != 0:
        print("╔══════════════════════════════╗")
        print("║       MENÚ PRINCIPAL         ║")
        print("╠══════════════════════════════╣")
        print("║      USUARIOS LOGUEADOS:     ║")
        print(f"║{usuarios:^30}║")
        print("╠══════════════════════════════╣")
        print("║ 1. Loguearse                 ║")
        print("║ 2. Jugar                     ║")
        print(f"║ 3. Dificultad: {dificultad} letras      ║")
        print("║ 4. Estadisticas              ║")
        print("║ 5. Cerrar sesión             ║")
        print("║ 6. Salir                     ║")
        print("╚══════════════════════════════╝")
    else:
        print("╔══════════════════════════════╗")
        print("║       MENÚ PRINCIPAL         ║")
        print("╠══════════════════════════════╣")
        print("║   NO HAY USUARIOS LOGUEADOS  ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Loguearse                 ║")
        print("║ 2. Jugar                     ║")
        print("║ 3. Seleccionar dificultad    ║")
        print("║ 4. Estadisticas              ║")
        print("║ 5. Desloguearse              ║")
        print("║ 6. Salir                     ║")
        print("╚══════════════════════════════╝")




def main(config:dict = { } ) -> dict:
    """
        Funcion de UI que integra las secciones
        - Estadisticas
        - Jugadores (loguear jugadores)
        - Dificultad
        - Jugar
        - Salir

        Cuando el usuario elige la opcion jugar la funcion termina de ejecutarse y devuelve un diccionario con el siguiente formato:
        {
            "salir": False,
            "dificultad":5,
            "jugadores": [{info jugador del JSON}, ...],
        }
        """
    salir = False
    dif = config.get("dificultad", 5)
    usuarios = config.get("jugadores", [])
    while True:
        menu(usuarios, dif)
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            if len(usuarios) > 0:
                usuarios = []
                print("╔═════════════════════════════════════════════════════╗")
                print("║ CERRANDO SESION DE USUARIO(S) Y VOLVIENDO A LOGUEAR ║")
                print("╚═════════════════════════════════════════════════════╝")
            usuarios = login.menu_login()
        elif opcion == "2":
            # SI FALTAN USUARIOS NO ARRANCA LA PARTIDA
            if len(usuarios) == 0:
                print("╔════════════════════════════════════════════════════════╗")
                print("║ Error: no hay usuarios para jugar, por favor loguearse ║")
                print("╚════════════════════════════════════════════════════════╝")
                continue
            else:
                break
        elif opcion == "3":
            dif = seleccionarDificultad()
        elif opcion == "4":
            ranking()
        elif opcion == "5":
            usuarios = []
            print("╔═════════════════════════════╗")
            print("║ CERRANDO SESION DE USUARIOS ║")
            print("╚═════════════════════════════╝")
        elif opcion == "6":
            salir = True
            print("╔════════════════════════╗")
            print("║    CERRANDO PROGRAMA   ║")
            print("║    GRACIAS POR JUGAR   ║")
            print("╚════════════════════════╝")
            break
        else:
            print("\nOpción inválida.")

    datos = {
        "jugadores": usuarios,
        "dificultad": dif,
        "salir": salir
    }
    return datos

    # prueba para que no falle el resto del programa
    ''' ASI TIENE QUE SALIR
    jugadores = gestion_datos.obtener_usuarios()[:1]
    return {
        "salir": False,
        "dificultad":5,
        "jugadores": jugadores,
    }
    '''


def repetir_partida() -> bool:
    print("╔═══════════════════════╗")
    print("║   PARTIDA FINALIZADA  ║")
    print("║ DESEA VOLVER A JUGAR? ║")
    print("╚═══════════════════════╝")
    decision = input("SI (S) o NO (N):")
    while decision not in ["S", "s", "N", "n"]:
        decision = input("SI (S) o NO (N):")
    decision = decision.upper()
    if decision == "S":
        return True
    else:
        return False



def convertirArriesgo(palabra_adivinar, arriesgo, adivinado: list):
    # Analiza el arriesgo para devolver el color en el que va a ir cada letra
    palabra_adivinar_arr = [*palabra_adivinar]
    arriesgo_arr = [*arriesgo]
    letras_sin_adivinar = []
    letras_sin_procesar = []
    resultado = {
        "Verde": [],
        "Amarillo": [],
        "GrisOscuro": [],
    }

    for index in range(len(arriesgo_arr)):
        if palabra_adivinar_arr[index] == arriesgo_arr[index]:
            resultado["Verde"].append(index)
        else:
            letras_sin_adivinar.append(palabra_adivinar_arr[index])
            letras_sin_procesar.append(arriesgo_arr[index])

    if len(letras_sin_procesar) > 0:
        for index in range(len(letras_sin_procesar.copy())):
            if letras_sin_procesar[index] in letras_sin_adivinar:
                resultado["Amarillo"].append(letras_sin_procesar[index])
                letras_sin_adivinar.remove(letras_sin_procesar[index])
            else:
                resultado["GrisOscuro"].append(letras_sin_procesar[index])
    mostrar = ""
    for i in range(len(arriesgo)):
        letra = arriesgo[i]

        if (i in resultado["Verde"]):
            mostrar += cambiar_color(letra.upper(), "Verde")
        elif (letra in resultado["Amarillo"]):
            resultado["Amarillo"].remove(letra)

            mostrar += cambiar_color(letra.upper(), "Amarillo")
        elif (letra in resultado["GrisOscuro"]):
            resultado["GrisOscuro"].remove(letra)

            mostrar += cambiar_color(letra.upper(), "GrisOscuro")

    return mostrar



def ronda(palabra_adivinar: str, dificultad: int, jugador: dict, letras_adivinadas: list, arriesgos: list, shows: list) -> str:
    if len(arriesgos) != 0:
        arriesgo = arriesgos[-1]
        for i in range(len(arriesgo)):
            if arriesgo[i] == palabra_adivinar[i]:
                letras_adivinadas[i] = cambiar_color(palabra_adivinar[i].upper(), "Verde")
        show = convertirArriesgo(palabra_adivinar, arriesgo, letras_adivinadas)
        shows.append(show)
    print("╔══════════════════════════════╗")
    print(f"║{alinear.centrar(f'ES EL TURNO DE {jugador.get("usuario").upper()}', 30)}║")
    print(" ═══════════════════════════════")
    print(f"║{alinear.centrar('PALABRA A ADIVINAR:',30)}║")
    print(f"║{alinear.centrar(' '.join(letras_adivinadas), 30)}║")
    print("╠══════════════════════════════╣")
    print(f"║{alinear.centrar('ARRIESGOS:',30)}║")
    for i in range(5):
        if i < len(shows):
            print(f"            {shows[i]}")
        else:
            print(f"          {"_ " * dificultad}           ")
    print(f"      QUEDAN {5 - len(arriesgos)} RESTANTES       ")
    print("╚══════════════════════════════╝")
    """
    Muestra la interfaz de la ronda y devuelve el intento del usuario

    TODO: hacer que se vea mejor
    TODO: hacer las validaciones correspondientes (que la cantidad de letras sea igual a la dificultad y normalizar los caracteres con tildes)
    """
    # logica.mostrar_letras_adivinadas(palabra_adivinar, letras_adivinadas)
    # logica.mostrar_arriesgos(arriesgos, dificultad)
    arri = input("ARRIESGO: ")
    while len(arri) != dificultad:
        arri = input(f"EL ARRIESGO DEBE TENER {dificultad} CARACTERES: ")

    return (arri.upper(), letras_adivinadas)


#@procedimiento
def partida_finalizada(datos_partida: dict) -> None:
    """
    Es una funcion de UI que informa al usuario que la partida ha sido finalizada y muestra los datos de la misma
    """
    print("=" * 50)
    print("🎉 PARTIDA FINALIZADA 🎉")
    print("=" * 50)

    # Información general de la partida
    tiempo_min, tiempo_seg = datos_partida['tiempo_total']
    print(f"⏱️  Tiempo total: {tiempo_min} minutos y {tiempo_seg} segundos")
    print(f"🎯 Palabra correcta: {datos_partida['palabra']}")

    # Información del ganador
    ganador = datos_partida['ganador']
    if ganador:
        # Información de todos los jugadores
        print(f"\n🏆 GANADOR: {ganador['usuario'].upper()}")
        print(f"   Intentos realizados: {ganador['intentos']}")
        print(f"\n👥 JUGADORES ({len(datos_partida['jugadores'])}):")
        for i, jugador in enumerate(datos_partida['jugadores'], 1):
            estado = "🏆 GANADOR" if jugador['id'] == ganador['id'] else "❌ No ganó"
            print(f"   {i}. {jugador['usuario']} - {jugador['intentos']} intentos - {estado}")
    else:
        print(f"\n❌ Nadie ganó la partida. ❌")

    # Intentos realizados durante la partida
    if datos_partida['arriesgos']:
        print(f"\n📝 INTENTOS REALIZADOS ({len(datos_partida['arriesgos'])}):")
        for i, intento in enumerate(datos_partida['arriesgos'], 1):
            print(f"   {i}. {intento}")

#test
if __name__ == "__main__":
    menu([{'id': 7, 'usuario': 'matias', 'contrasena': 'Matias1234', 'puntaje': 380, 'total_partidas': 9, 'total_primeros_turnos': 0, 'palabras_usadas': 'DUNAS'},], 5)