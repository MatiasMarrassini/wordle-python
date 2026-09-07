import datos
from UI.decorador_procedimientos import procedimiento

#@procedimiento
def ranking():
    """
    Tomar datos usando la función gestion_datos.obtener_usuarios()
    En base a los usuarios muestra una tabla con el top de jugadores ordenados verticalmente por puntaje
    """
    try:
        # Obtener datos de usuarios
        usuarios = datos.obtener_usuarios()

        # Verificar si hay usuarios
        if not usuarios:
            print("No hay usuarios registrados.")
            return

        # Ordenar usuarios por puntaje de mayor a menor
        usuarios_ordenados = sorted(usuarios, key=lambda x: x['puntaje'], reverse=True)

        # Mostrar encabezado de la tabla
        print("\n" + "=" * 60)
        print("🏆 RANKING DE JUGADORES 🏆")
        print("=" * 60)
        print(f"{'Pos':<4} {'Usuario':<15} {'Puntaje':<10} {'Partidas':<10} {'1° Turnos':<10}")
        print("-" * 60)

        # Mostrar cada jugador en la tabla
        for i, usuario in enumerate(usuarios_ordenados, 1):
            posicion = f"{i}°"
            nombre = usuario['usuario']
            puntaje = usuario['puntaje']
            partidas = usuario['total_partidas']
            primeros_turnos = usuario['total_primeros_turnos']

            # Agregar emoji para los primeros 3 lugares
            if i == 1:
                posicion = "🥇"
            elif i == 2:
                posicion = "🥈"
            elif i == 3:
                posicion = "🥉"

            print(f"{posicion:<4} {nombre:<15} {puntaje:<10} {partidas:<10} {primeros_turnos:<10}")

        print("-" * 60)
        print(f"Total de jugadores: {len(usuarios_ordenados)}")
        print("=" * 60)

    except Exception as e:
        print(f"Error al mostrar el ranking: {e}")


# Función adicional para mostrar ranking con más detalles
def ranking_detallado():
    """
    Versión más detallada del ranking que incluye palabras usadas
    """
    try:
        usuarios = datos.obtener_usuarios()

        if not usuarios:
            print("No hay usuarios registrados.")
            return

        usuarios_ordenados = sorted(usuarios, key=lambda x: x['puntaje'], reverse=True)

        print("\n" + "=" * 80)
        print("🏆 RANKING DETALLADO DE JUGADORES 🏆")
        print("=" * 80)

        for i, usuario in enumerate(usuarios_ordenados, 1):
            posicion = f"{i}°"
            if i == 1:
                posicion = "🥇"
            elif i == 2:
                posicion = "🥈"
            elif i == 3:
                posicion = "🥉"

            print(f"\n{posicion} {usuario['usuario'].upper()}")
            print(f"   Puntaje: {usuario['puntaje']} puntos")
            print(f"   Partidas jugadas: {usuario['total_partidas']}")
            print(f"   Primeros turnos: {usuario['total_primeros_turnos']}")

            # Mostrar palabras usadas (máximo 5 para no saturar)
            palabras = usuario['palabras_usadas']
            if palabras:
                palabras_mostrar = palabras[:5] if len(palabras) > 5 else palabras
                print(f"   Palabras usadas: {', '.join(palabras_mostrar)}")
                if len(palabras) > 5:
                    print(f"   ... y {len(palabras) - 5} más")
            else:
                print("   Palabras usadas: Ninguna")

            print("-" * 40)

        print(f"\nTotal de jugadores: {len(usuarios_ordenados)}")
        print("=" * 80)

    except Exception as e:
        print(f"Error al mostrar el ranking detallado: {e}")


# Función para mostrar solo el top N jugadores
def top_jugadores(n=5):
    """
    Muestra solo los primeros N jugadores del ranking
    """
    try:
        usuarios = datos.obtener_usuarios()

        if not usuarios:
            print("No hay usuarios registrados.")
            return

        usuarios_ordenados = sorted(usuarios, key=lambda x: x['puntaje'], reverse=True)
        top_n = usuarios_ordenados[:n]

        print(f"\n🏆 TOP {n} JUGADORES 🏆")
        print("=" * 50)
        print(f"{'Pos':<4} {'Usuario':<15} {'Puntaje':<10} {'Partidas':<10}")
        print("-" * 50)

        for i, usuario in enumerate(top_n, 1):
            posicion = f"{i}°"
            if i == 1:
                posicion = "🥇"
            elif i == 2:
                posicion = "🥈"
            elif i == 3:
                posicion = "🥉"

            print(f"{posicion:<4} {usuario['usuario']:<15} {usuario['puntaje']:<10} {usuario['total_partidas']:<10}")

        print("=" * 50)

    except Exception as e:
        print(f"Error al mostrar el top de jugadores: {e}")


# Ejemplo de uso
if __name__ == "__main__":
    # Llamar a la función principal
    ranking()

    # Opcional: mostrar ranking detallado
    # ranking_detallado()

    # Opcional: mostrar solo top 3
    # top_jugadores(3)