from excepciones import RelojException
from modoReloj import ModoReloj

class Normal(ModoReloj):

    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        print(mensaje)
   
            
        