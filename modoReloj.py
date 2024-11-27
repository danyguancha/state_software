from abc import ABC, abstractmethod

class ModoReloj(ABC):

    @abstractmethod
    def mostrar_mensaje(self, mensaje:str, tipoMensaje:str):
        pass

    def obtenerMedida(self, nombreMedida:str):
        pass
