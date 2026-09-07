import re

def _longitud_visible(texto):
    return len(re.sub(r'\x1b\[[0-9;]*m', '', texto))

def centrar(mensaje:str, espacio:int) -> str:
    longitud_visible = _longitud_visible(mensaje)
    if longitud_visible >= espacio:
        return mensaje
    izq = (espacio - longitud_visible) // 2
    der = espacio - longitud_visible - izq
    return ' ' * izq + mensaje + ' ' * der

def izquierda(mensaje:str, espacio:int) -> str:
    longitud_visible = _longitud_visible(mensaje)
    if longitud_visible >= espacio:
        return mensaje
    relleno = espacio - longitud_visible
    return mensaje + ' ' * relleno

def derecha(mensaje:str, espacio:int) -> str:
    longitud_visible = _longitud_visible(mensaje)
    if longitud_visible >= espacio:
        return mensaje
    relleno = espacio - longitud_visible
    return ' ' * relleno + mensaje

if __name__ == "__main__":
    letras = ['_', '\x1b[32mE\x1b[39m', '\x1b[32mR\x1b[39m', '\x1b[32mD\x1b[39m', '\x1b[32mI\x1b[39m']
    mensaje = " ".join(letras)

    print(f"|{izquierda(mensaje, 30)}|  ← izquierda")
    print(f"|{centrar(mensaje, 30)}|  ← centrado")
    print(f"|{derecha(mensaje, 30)}|  ← derecha")