from excepciones import RelojException
from modoReloj import ModoReloj

class Normal(ModoReloj):

    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        print(mensaje)

    def obtener_medida(self, nombre_medida:str, reloj):
        return reloj.medidas.get(nombre_medida)
   
            
        