from unittest import TestCase

from excepciones import RelojException
from reloj import Reloj, Modo


class TestReloj(TestCase):
    def test_obtener_medidas_modo_normal(self):
        reloj = Reloj("Madera")
        valor_pasos = reloj.obtener_medida("pasos")
        self.assertIsNone(valor_pasos)
        reloj.adicionar_medida("pasos", 100)
        valor_pasos = reloj.obtener_medida("pasos")
        self.assertEqual(100, valor_pasos)

    def test_obtener_medidas_modo_ejercicio(self):
        reloj = Reloj("Madera")
        reloj.cambiar_modo(Modo.EJERCICIO)
        valor_pasos = reloj.obtener_medida("pasos")
        self.assertIsNone(valor_pasos)
        reloj.adicionar_medida("pasos", 100)
        valor_pasos = reloj.obtener_medida("pasos")
        self.assertEqual(100, valor_pasos)

    def test_obtener_medidas_modo_reposo(self):
        reloj = Reloj("Madera")
        reloj.cambiar_modo(Modo.REPOSO)
        with self.assertRaises(RelojException):
            reloj.obtener_medida("pasos")

    def test_color_fondo_normal(self):
        reloj = Reloj("Madera")
        self.assertEqual("blanco", reloj.color_fondo)

    # def test_color_fondo_ejercicio(self):
    #     reloj = Reloj("Madera")
    #     reloj.cambiar_modo(Modo.EJERCICIO)
    #     self.assertEqual("azul", reloj.color_fondo)
    #
    # def test_color_fondo_reposo(self):
    #     reloj = Reloj("Madera")
    #     reloj.color_fondo(Modo.REPOSO)
    #     self.assertEqual("blanco", reloj.color_fondo)




