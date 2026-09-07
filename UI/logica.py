"""
En este archivo se alojan las funciones relacionadas con la logica de la interfaz
"""

from functools import reduce
import utils


def procesar_intento(palabra_adivinar: str, arriesgo: str):
    """Analiza el arriesgo para devolver el color en el que va a ir cada letra"""

    palabra_adivinar_arr = list(palabra_adivinar)
    arriesgo_arr = list(arriesgo)
    resultado = {
        "verde": [],
        "amarillo": [],
        "grisOscuro": [],
    }

    # identificar posiciones correctas (verde)
    resultado["verde"] = list(
        filter(
            lambda i: palabra_adivinar_arr[i] == arriesgo_arr[i],
            range(len(arriesgo_arr)),
        )
    )

    # obtener letras que no coincidieron en posición
    indices_no_verdes = list(
        filter(lambda i: i not in resultado["verde"], range(len(arriesgo_arr)))
    )

    letras_sin_adivinar = list(
        map(lambda i: palabra_adivinar_arr[i], indices_no_verdes)
    )
    letras_sin_procesar = list(map(lambda i: arriesgo_arr[i], indices_no_verdes))

    # Procesar letras amarillas y grises
    for letra in letras_sin_procesar.copy():
        if letra in letras_sin_adivinar:
            resultado["amarillo"].append(letra)
            letras_sin_adivinar.remove(letra)
        else:
            resultado["grisOscuro"].append(letra)

    return resultado


def procesar_arriesgo(palabra, arriesgo, adivinado):
    """procesa el arriesgo y lo clasifica por color"""
    resultado = procesar_intento(palabra, arriesgo)
    mostrar = ""

    for i in range(len(arriesgo)):
        letra = arriesgo[i]

        if i in resultado["verde"]:
            mostrar += utils.cambiar_color(letra, "verde")
            if not i in adivinado:
                adivinado.append(i)
        elif letra in resultado["amarillo"]:
            resultado["amarillo"].remove(letra)
            mostrar += utils.cambiar_color(letra, "amarillo")
        elif letra in resultado["grisOscuro"]:
            resultado["grisOscuro"].remove(letra)

            mostrar += utils.cambiar_color(letra, "grisOscuro")

    return mostrar

def validar_arriesgo(arriesgo):
    valido = False
    len_correcto = True
    LEN_CORRECTO = 5

    if len(arriesgo) != LEN_CORRECTO:
        print("El arriesgo debe tener 5 caracteres")
        len_correcto = False

    # Verifica que sean solo letras
    if len_correcto:
        if arriesgo.isalpha():
            valido = True
        else:
            print("El arriesgo debe contener solo letras")

    return valido


def normalizar_letras(s):
    sustitutos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    # Usar reduce para aplicar todos los reemplazos
    return reduce(
        lambda acc, repl: acc.replace(repl[0], repl[1]), sustitutos, s
    ).upper()
    
    
def mostrar_arriesgos(arriesgos, intentos):
    CANTIDAD_MAXIMA_ARRIESGOS = intentos

    for i in range(CANTIDAD_MAXIMA_ARRIESGOS):
        print(arriesgos[i] if i < len(arriesgos) else "?????")


def mostrar_letras_adivinadas(palabra, adivinado):
    LARGO_PALABRA = 5
    print("PALABRA A ADIVINAR: ", end="")
    for i in range(LARGO_PALABRA):
        if i in adivinado:
            print(utils.cambiar_color(palabra[i], "Verde"), end="")
        else:
            print("?", end="")

    print(" ")