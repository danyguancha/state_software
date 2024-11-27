from celular import Celular
from reloj import Reloj, Modo

if __name__ == '__main__':
    celular = Celular("gato")
    reloj = Reloj("Madera")
    reloj.adicionar_medida("pasos", 500)
    reloj.adicionar_medida("presión", 70)
    celular.reloj_asociado = reloj

    print("---EN MODO NORMAL---")
    celular.llamada_entrante()
    celular.alarma()
    #celular.mostrar_medidas()
    print()

    print("---EN MODO EJERCICIO---")
    reloj.cambiar_modo(Modo.EJERCICIO)
    celular.llamada_entrante()
    celular.alarma()
    #celular.mostrar_medidas()
    print()

    print("---EN MODO REPOSO---")
    reloj.cambiar_modo(Modo.REPOSO)
    celular.llamada_entrante()
    celular.alarma()
    #celular.mostrar_medidas()
    print()


