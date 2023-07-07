from clases.Ruta import *

def verificarNumeroRouter(numeroRouter, ruta: Ruta):
    if numeroRouter in range (1, len(ruta.routers)):
        return True
    else:
        return False
    
def verificarNumeroInput(texto1):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            if varInt!=None:
                break
            else:
                print("Ingreso invalido. Por favor, inténtelo de nuevo.")
        except ValueError:
            print("Ingreso invalido. Por favor, inténtelo de nuevo.")
    return varInt