from enum import Enum

from normal import Normal
from ejercicio import Ejercicio
from reposo import Reposo


class Modo(Enum):
    """
    Formas de uso de un reloj inteligente.
    """
    NORMAL = 1
    EJERCICIO = 2
    REPOSO = 3

class Reloj:
    def __init__(self, material:str):
        self.material = material
        #self.modo = Modo.NORMAL
        self.color_fondo = "blanco"
        self.medidas = {}
        
        self.modos = {
            Modo.NORMAL: Normal(),
            Modo.EJERCICIO: Ejercicio(),
            Modo.REPOSO: Reposo()
        }
        self.modo_actual = self.modos[Modo.NORMAL]

    def mostrar_mensaje(self, mensaje:str, tipo_mensaje:str):
        """
        Muestra un mensaje enviado por el celular.
        Dependiendo del modo puede mostrar (o no) algunos tipos de mensajes.
        """
        self.modo_actual.mostrar_mensaje(mensaje, tipo_mensaje)
        
     


    def cambiar_modo(self, nuevo_modo:Modo):
        self.modo = self.modos[nuevo_modo]

    def obtener_medida(self, nombre_medida:str) -> float:

        return self.modo_actual.obtener_medida(nombre_medida, self)

    def adicionar_medida(self, nombre_medida:str, valor:float):
        self.medidas[nombre_medida] = valor
        