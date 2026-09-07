def obtener_color(color) -> str:
    """
    devuelve el codigo del color indicado
    """
    colores = {
        "verde": "\x1b[32m",
        "amarillo": "\x1b[33m",
        "grisOscuro": "\x1b[90m",
        "defecto": "\x1b[39m",
        "rojo": "\033[91m",
        "azul": "\33[34m"
    }
    return colores.get(color.lower(), "\x1b[39m") #si no encuentra el color devuelve "\x1b[39m" para evitar errores

def cambiar_color(texto, color):
    return (obtener_color(color) + texto + obtener_color("Defecto")) if texto != "" else ""


if __name__ == "__main__":
    letras_adivinadas = ['_', '\x1b[32mE\x1b[39m', '\x1b[32mR\x1b[39m', '\x1b[32mD\x1b[39m', '\x1b[32mI\x1b[39m']
    print(f"| {(letras_adivinadas):^30} |")