from auxiliares import *
from clases.Ruta import *

def agregarRouterARuta(ruta: Ruta):
    cantRouters=len(ruta.routers)
    nombreRouter="router_"+str(cantRouters+1)
    router=Router(nombreRouter)
    ruta.agregarRouter(router)
    
def activarRouter(ruta: Ruta):
    mensaje="Ingrese el numero del router que desea activar o -1 para volver al menu: "
    numeroRouter=validarIngresoNumerico(mensaje)
    if numeroRouter == -1:
        return False
    while not verificarNumeroRouter(numeroRouter, ruta):
        mensaje="Router inexistente. Ingrese nuevamente el numero del router que desea activar o -1 para volver al menu: "
        numeroRouter=validarIngresoNumerico(mensaje)
        if numeroRouter == -1:
            return False
    ruta.routers[numeroRouter-1].activar()

def desactivarRouter(ruta: Ruta):
    mensaje="Ingrese el numero del router que desea desactivar o -1 para volver al menu: "
    numeroRouter=validarIngresoNumerico(mensaje)
    if numeroRouter == -1:
        return False
    while not verificarNumeroRouter(numeroRouter, ruta):
        mensaje="Router inexistente. Ingrese nuevamente el numero del router que desea desactivar o -1 para volver al menu: "
        numeroRouter=validarIngresoNumerico(mensaje)
        if numeroRouter == -1:
            return False
    ruta.routers[numeroRouter-1].desactivar()

def mostrarRuta(ruta: Ruta):
    if len(ruta.routers) == 0:
        print("La ruta no tiene routers")
    else:
        print("La ruta tiene los siguientes routers:")
        for router in ruta.routers:
            print(router)