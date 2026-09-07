def procedimiento(func) -> callable:
    """
    es un decorador de funciones que impide que las funciones de UI que no piden datos al usuario desaparezcan antes de que el usuario presione enter
    """
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        input("-Enter para continuar-")
        
    return wrapper



if __name__ == "__main__":
    @procedimiento
    def saludo():
        print("Hola mundo!")

    saludo()