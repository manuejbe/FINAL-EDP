from auxiliares import *
from clases.Ruta import *
from clases.Router import *
from clases.RoutingSim import *
from clases.Paquete import Paquete
#importar clase paquete

def agregarRouterARuta(ruta: Ruta):
    cantRouters=len(ruta.routers)
    nombreRouter="router_"+str(cantRouters+1)
    router=Router(nombreRouter)
    ruta.agregarRouter(router)
    
def activarRouter(ruta: Ruta):
    mensaje="Ingrese el numero del router que desea activar o -1 para volver al menu: "
    numeroRouter=verificarNumeroInput(mensaje)
    if numeroRouter == -1:
        return False
    while not verificarNumeroRouter(numeroRouter, ruta):
        mensaje="Router inexistente. Ingrese nuevamente el numero del router que desea activar o -1 para volver al menu: "
        numeroRouter=verificarNumeroInput(mensaje)
        if numeroRouter == -1:
            return False
    ruta.routers[numeroRouter-1].activar()

def desactivarRouter(ruta: Ruta):
    mensaje="Ingrese el numero del router que desea desactivar o -1 para volver al menu: "
    numeroRouter=verificarNumeroInput(mensaje)
    if numeroRouter == -1:
        return False
    while not verificarNumeroRouter(numeroRouter, ruta):
        mensaje="Router inexistente. Ingrese nuevamente el numero del router que desea desactivar o -1 para volver al menu: "
        numeroRouter=verificarNumeroInput(mensaje)
        if numeroRouter == -1:
            return False
    ruta.routers[numeroRouter-1].desactivar()

def mostrarRuta(ruta: Ruta):
        print(ruta)

def simularRuta(ruta: Ruta):
    tiempoSimulacion=verificarNumeroInput("Ingrese el tiempo de simulacion en segundos: ")
    while tiempoSimulacion < 0:
        tiempoSimulacion=verificarNumeroInput("Ingrese un tiempo de simulacion valido: ")
    cantidadPaquetes=verificarNumeroInput("Ingrese la cantidad de paquetes a enviar: ")
    while cantidadPaquetes < 0:
        cantidadPaquetes=verificarNumeroInput("Ingrese una cantidad de paquetes valida: ")
    paquetes=[]
    for i in range(cantidadPaquetes):
        print(f"Paquete {i+1}:")
        origen=verificarNumeroInput("Ingrese el numero del router origen: ")
        destino=verificarNumeroInput("Ingrese el numero del router destino: ")
        contenido=input("Ingrese el contenido del paquete: ")
        paquete=Paquete(origen, destino, contenido)
        paquetes.append(paquete)
    routingSim=RoutingSim(tiempoSimulacion, ruta, paquetes)