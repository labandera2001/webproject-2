import unittest

import requests


class MyTestCase(unittest.TestCase):

    def test_sumar(self):
        respuesta = requests.get("http://localhost/calculadora/2/sumar/2")
        assert respuesta.text == "4", f"resultado invalido {respuesta.text}"

    def test_restar(self):
        respuesta = requests.get("http://localhost/calculadora/2/restar/2")
        assert respuesta.text == "0", f"resultado invalido {respuesta.text}"

    def test_multiplicar(self):
        respuesta = requests.get("http://localhost/calculadora/2/multiplicar/2")
        assert respuesta.text == "4", f"resultado invalido {respuesta.text}"

    def test_dividir(self):
        respuesta = requests.get("http://localhost/calculadora/2/dividir/2")
        assert float(respuesta.text) == float("1"), f"resultado invalido {respuesta.text}"

if __name__ == '__main__':
    unittest.main()