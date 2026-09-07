import unittest
from juego import logica
from unittest.mock import patch
import time

class TestLogicaJuego(unittest.TestCase):

    def test_calcular_tiempo_total(self):
        tiempo_inicial = time.time() - 125  # Simula que pasaron 2 min y 5 seg
        minutos, segundos = logica.calcular_tiempo_total(tiempo_inicial)
        self.assertEqual(minutos, 2)
        self.assertEqual(segundos, 5)

    @patch("juego.logica.obtener_palabras")
    @patch("random.randint", return_value=0)
    def test_conseguir_palabra(self, mock_randint, mock_obtener_palabras):
        mock_obtener_palabras.return_value = ["perro", "gato", "raton"]
        usadas = ["gato"]
        palabra = logica.conseguir_palabra(5, usadas)

        self.assertIn(palabra.lower(), ["perro", "raton"])
        self.assertNotEqual(palabra.lower(), "gato")
        self.assertTrue(palabra.isupper())

    def test_acomodar_jugadores(self):
        jugadores = [
            {"nombre": "Ana", "total_primeros_turnos": 1},
            {"nombre": "Luis", "total_primeros_turnos": 3},
            {"nombre": "Marta", "total_primeros_turnos": 2},
        ]
        ordenados = logica.acomodar_jugadores(jugadores)
        nombres = [j["nombre"] for j in ordenados]
        self.assertEqual(nombres, ["Luis", "Marta", "Ana"])

        # Asegura que la lista original no se modificó
        self.assertEqual(jugadores[0]["nombre"], "Ana")


if __name__ == '__main__':
    unittest.main()
