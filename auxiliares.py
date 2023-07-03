from clases.Ruta import *

def verificarNumeroRouter(numeroRouter, ruta: Ruta):
    if numeroRouter in range (1, len(ruta.routers)):
        return True
    else:
        return False