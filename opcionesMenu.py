from auxiliares import *
from clases.Ruta import *
from clases.Router import *
from clases.RoutingSim import *
from clases.Paquete import Paquete

def agregarRouterARuta(ruta: Ruta):
    cantRouters=ruta.len
    router=Router(cantRouters+1)
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
    router = ruta.head
    for i in range(numeroRouter):
        router = router.siguiente
    router = router.activar()

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
    router = ruta.head
    for i in range(numeroRouter):
        router = router.siguiente
    router = router.desactivar()

def mostrarRuta(ruta: Ruta):
        print(ruta)

async def simularRuta(ruta: Ruta):
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
    await routingSim.simular()