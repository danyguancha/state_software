from excepciones import RelojException
from modoReloj import ModoReloj
class Ejercicio(ModoReloj):
    
    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        if tipoMensaje == "llamada":
            print(mensaje)
        else:
            raise RelojException("No se puede mostrar el mensaje de tipo {tipoMensaje} en modo de ejercicio")