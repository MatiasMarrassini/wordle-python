from juego import partida
import UI
import datos


def main():

    configuracion = datos.cargar_configuracion()

    while True:
        configuracion = UI.main(configuracion)

        jugadores = configuracion.get("jugadores")
        dificultad = configuracion.get("dificultad")
        salir = configuracion.get("salir")
        if salir:
            break

        # jugar partida
        continuar_partida = True
        while continuar_partida:
            datos_partida = partida(jugadores, dificultad)

            UI.partida_finalizada(datos_partida)
            datos.registrar_datos_partida(datos_partida)  # funcion de mati

            continuar_partida = UI.repetir_partida()
            jugadores = datos_partida["jugadores"]  # para que se apliquen palabras_usadas y total_primeros_turnos, indispensables

    datos.guardar_configuracion(configuracion)

if __name__ == "__main__":
    main()
