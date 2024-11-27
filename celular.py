from excepciones import RelojException
from reloj import Reloj


class Celular:
    """
    Celular inteligente que puede comunicarse con un reloj
    para obtener o mostrar información
    """
    def __init__(self, marca:str):
        self.marca = marca
        self.reloj_asociado = None

    def asociar_reloj(self, reloj:Reloj):
        self.reloj_asociado = reloj

    def mostrar_medidas(self):
        """
        Muestra un conjunto básico de medidas del reloj
        """
        if self.reloj_asociado is not None:
            try:
                print("Pasos: " + str(self.reloj_asociado.obtener_medida("pasos")))
                print("Presión: "+ str(self.reloj_asociado.obtener_medida("presión")))
            except RelojException as error_medida:
                print(error_medida)
        else:
            print("No hay reloj asociado")

    def llamada_entrante(self):
        if self.reloj_asociado is not None:
            print("Se envía llamada al reloj")
            self.reloj_asociado.mostrar_mensaje("Llamada entrante","llamada")

    def alarma(self):
        if self.reloj_asociado is not None:
            print("Se envía alarma al reloj")
            self.reloj_asociado.mostrar_mensaje("Una alarma","alarma")
