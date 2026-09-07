import unittest
from UI import logica
from unittest.mock import patch

class TestUILogica(unittest.TestCase):

    def test_procesar_intento(self):
        palabra = "SALTA"
        intento = "SAPOS"
        resultado = logica.procesar_intento(palabra, intento)

        self.assertEqual(resultado["verde"], [0, 1])
        self.assertIn("A", resultado["amarillo"])
        self.assertIn("P", resultado["grisOscuro"])
        self.assertIn("O", resultado["grisOscuro"])
        self.assertIn("S", resultado["grisOscuro"])  # La segunda S no matchea

    @patch("utils.cambiar_color")
    def test_procesar_arriesgo(self, mock_cambiar_color):
        mock_cambiar_color.side_effect = lambda letra, color: f"<{color}:{letra}>"
        palabra = "TIGRE"
        arriesgo = "TREPA"
        adivinado = []

        resultado = logica.procesar_arriesgo(palabra, arriesgo, adivinado)
        esperado = "<verde:T><amarillo:R><amarillo:E><grisOscuro:P><grisOscuro:A>"
        self.assertEqual(resultado, esperado)
        self.assertIn(0, adivinado)  # T en la posición correcta

    def test_validar_arriesgo_valido(self):
        self.assertTrue(logica.validar_arriesgo("PERRO"))

    def test_validar_arriesgo_invalido_por_longitud(self):
        with self.assertLogs(level='INFO') as cm:
            self.assertFalse(logica.validar_arriesgo("PERROS"))

    def test_validar_arriesgo_invalido_por_caracteres(self):
        self.assertFalse(logica.validar_arriesgo("PER4O"))

    def test_normalizar_letras(self):
        palabra = "párénísís"
        resultado = logica.normalizar_letras(palabra)
        self.assertEqual(resultado, "PARENISIS")

    @patch("builtins.print")
    def test_mostrar_arriesgos(self, mock_print):
        arriesgos = ["PRUEB", "OTRO1"]
        logica.mostrar_arriesgos(arriesgos, 4)
        mock_print.assert_any_call("PRUEB")
        mock_print.assert_any_call("OTRO1")
        mock_print.assert_any_call("?????")

    @patch("utils.cambiar_color")
    @patch("builtins.print")
    def test_mostrar_letras_adivinadas(self, mock_print, mock_color):
        mock_color.side_effect = lambda letra, color: f"<{color}:{letra}>"
        palabra = "CASCO"
        adivinado = [0, 2, 4]
        logica.mostrar_letras_adivinadas(palabra, adivinado)
        mock_print.assert_any_call("<Verde:C><Verde:S><Verde:O>", end="")


if __name__ == '__main__':
    unittest.main()
