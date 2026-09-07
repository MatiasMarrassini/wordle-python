import unittest
import re
from UI.alinear import centrar, izquierda, derecha

def strip_ansi(texto):
    return re.sub(r'\x1b\[[0-9;]*m', '', texto)

class TestAlinearFunciones(unittest.TestCase):
    def test_centrar(self):
        msg = "_ \x1b[32mA\x1b[39m \x1b[31mB\x1b[39m"
        result = centrar(msg, 20)
        self.assertEqual(len(strip_ansi(result)), 20)

    def test_izquierda(self):
        msg = "\x1b[32mX\x1b[39m _"
        result = izquierda(msg, 15)
        self.assertTrue(strip_ansi(result).startswith('X'))
        self.assertEqual(len(strip_ansi(result)), 15)

    def test_derecha(self):
        msg = "_ \x1b[34mZ\x1b[39m"
        result = derecha(msg, 10)
        self.assertTrue(strip_ansi(result).endswith('Z'))
        self.assertEqual(len(strip_ansi(result)), 10)
