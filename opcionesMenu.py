from auxiliares import *
from clases.Ruta import *

def agregarRouterARuta(ruta: Ruta):
    cantRouters=len(ruta.routers)
    nombreRouter="router_"+str(cantRouters+1)
    router=Router(nombreRouter)
    ruta.agregarRouter(router)
    
def activarRouter(ruta: Ruta):
    nombreRouter=input("Ingrese el numero del router que desea activar o Z para volver al menu: ")
    if nombreRouter == "Z":
        return False
    while not verificarNumeroRouter(nombreRouter, ruta):
        nombreRouter=input("Router inexistente. Ingrese nuevamente el numero del router que desea activar o Z para volver al menu: ")
        if nombreRouter == "Z":
            return False
    ruta.routers[nombreRouter-1].activar()

def desactivarRouter(ruta: Ruta):
    nombreRouter=input("Ingrese el numero del router que desea desactivar o Z para volver al menu: ")
    if nombreRouter == "Z":
        return False
    while not verificarNumeroRouter(nombreRouter, ruta):
        nombreRouter=input("Router inexistente. Ingrese nuevamente el numero del router que desea desactivar o Z para volver al menu: ")
        if nombreRouter == "Z":
            return False
    ruta.routers[nombreRouter-1].desactivar()

def mostrarRuta(ruta: Ruta):
    if len(ruta.routers) == 0:
        print("La ruta no tiene routers")
    else:
        print("La ruta tiene los siguientes routers:")
        for router in ruta.routers:
            print(router)