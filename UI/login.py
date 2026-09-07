import autenticacion

def menu_login():
    usuario = autenticacion.login()
    if usuario == None:
        print("╔═════════════════════════════════════════════════════════╗")
        print("║ ERROR AL LOGUEAR AL USUARIO, VOLVIENDO AL MENU PRINCIPAL║")
        print("╚═════════════════════════════════════════════════════════╝")
        return []
    print ("Usuario 1 logueado con exito")
    opcion = input("Desea loguear un segundo usuario (S/N):")
    opcion = opcion.upper()
    while opcion != "N" and opcion != "S":
        opcion = input("Desea loguear un segundo usuario (S/N):")
        opcion = opcion.upper()
    if opcion == "S":
        usuario2 = autenticacion.login()
        if usuario2 == None:
            print("╔═════════════════════════════════════════════════════════════════╗")
            print("║ ERROR AL LOGUEAR AL SEGUNDO USUARIO, VOLVIENDO AL MENU PRINCIPAL║")
            print("╚═════════════════════════════════════════════════════════════════╝")
            return []
        return [usuario, usuario2]
    return [usuario]