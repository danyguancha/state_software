
from modoReloj import ModoReloj

class Reposo(ModoReloj):
    
    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        if tipoMensaje == "alarma":
            print(mensaje)
        