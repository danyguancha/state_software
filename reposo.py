
from excepciones import RelojException
from modoReloj import ModoReloj

class Reposo(ModoReloj):
    
    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        if tipoMensaje == "alarma":
            print(mensaje)

    def obtener_medida(self, nombre_medida:str, reloj):
        raise RelojException("No se pueden obtener medidas en modo de reposo")

    
        