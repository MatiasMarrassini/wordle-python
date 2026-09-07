
"""
Desde esta sección se maneja todas las funciones relacionadas con el registro de usuarios.
"""

import json
import os
import re


# Archivo donde se guardan los datos
if __name__ == "__main__":
    ARCHIVO_USUARIOS = '../datos/Usuarios.json'
else:
    ARCHIVO_USUARIOS = './datos/Usuarios.json'


# Cargar los usuarios del archivo JSON (si existe)
def cargar_usuarios():
    with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

# Guardar usuarios al archivo
def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, indent=2, ensure_ascii=False)

# Buscar un usuario por nombre
def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario['usuario'] == nombre:
            return usuario
    return None

def validar_contrasena(contrasena):
    # Longitud entre 8 y 16
    if not re.fullmatch(r'.{8,16}$', contrasena):
        print("❌La contraseña debe tener entre 8 y 16 caracteres.❌")
        return False

    # Al menos una mayúscula
    if not re.search(r'[A-Z]+', contrasena):
        print("❌Debe contener al menos una letra mayúscula.❌")
        return False

    # Al menos una minúscula
    if not re.search(r'[a-z]+', contrasena):
        print("❌Debe contener al menos una letra minúscula.❌")
        return False

    # Al menos un número
    if not re.search(r'[0-9]+', contrasena):
        print("Debe contener al menos un número.")
        return False
    print("✅Contraseña Valida✅")
    return True

def validar_usuario(nombre_usuario):
    patron = r'^[a-z]{4,20}$'
    if re.fullmatch(patron, nombre_usuario):
        print("✅Usuario Valido✅")
        return True
    else:
        print("❌El usuario debe tener solo letras minúsculas y entre 4 y 20 caracteres.❌")
        return False

# Lógica de login
def login():
    usuarios = cargar_usuarios()

    nombre = input("Nombre de usuario: ")
    while not validar_usuario(nombre):
        nombre = input("Nombre de usuario: ")
    usuario = buscar_usuario(usuarios, nombre)

    if usuario:
        contrasena = input("Usuario encontrado, ingrese contraseña: ")
        it = 3
        while usuario['contrasena'] != contrasena:
            it -= 1
            print(f"❌ Contraseña incorrecta. Quedan {it} intentos❌")
            if it == 0:
                print("❌ Demasiados intentos. El usuario se ha desconectado.❌")
                return None
            contrasena = input("Ingrese Contraseña: ")
        print(f"✅ Bienvenido de nuevo, {nombre}. Puntaje actual: {usuario['puntaje']}✅")
    else:
        #ACA APLICAREMOS RECURSIVIDAD DE PREGUNTAR SI QUEREMOS REGISTRARNOS O INICIAR SESION CON OTRO USUARIO LLAMANDO DE NUEVO A LOGIN
        print(f"🆕 Usuario no encontrado. Creando nuevo usuario {nombre}🆕")
        print("🔑Ahora debe ingresar su contraseña🔑")
        print("💡La contraseña deberá tener un minimo de 8 caracteres, al menos una mayúscula, una minúscula y un número💡")
        contrasena = input("Ingrese contraseña: ")
        while not validar_contrasena(contrasena):
            print("💡La contraseña deberá tener un minimo de 8 caracteres, al menos una mayúscula, una minúscula y un número💡")
            contrasena = input("Ingrese contraseña: ")
        nuevo_usuario = {
            "id" : len(usuarios)+1,
            "usuario": nombre,
            "contrasena": contrasena,
            "puntaje": 0,
            "total_partidas": 0,
            "total_primeros_turnos": 0,
            "palabras_usadas": []
        }
        usuarios.append(nuevo_usuario)
        guardar_usuarios(usuarios)
        print(f"💾 El usuario {nombre} con contraseña {contrasena} creado exitosamente.")
        usuario = nuevo_usuario

    return usuario  # Retornar el diccionario del usuario logueado

'''
# Prueba del login
usuario_actual = login()
if usuario_actual:
    print(f"👉🏿 Puedes comenzar a jugar, {usuario_actual['usuario']}.👈🏿")
'''

###########################################


'''
# Solicitar al usuario la contraseña
while True:
    contraseña = input("Introduce una contraseña: ")
    if validar_contraseña(contraseña):
        print("Contraseña válida.")
        break
    else:
        print("La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un número y un carácter especial.")
'''

