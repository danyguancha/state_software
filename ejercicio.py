from excepciones import RelojException
from modoReloj import ModoReloj
class Ejercicio(ModoReloj):
    
    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        if tipoMensaje == "llamada":
            print(mensaje)

        
    def obtener_medida(self, nombre_medida:str, reloj):
        return reloj.medidas.get(nombre_medida)