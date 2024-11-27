from abc import ABC, abstractmethod

class ModoReloj(ABC):

    @abstractmethod
    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        pass

    @abstractmethod
    def obtener_medida(self, nombre_medida:str, reloj):
        pass
