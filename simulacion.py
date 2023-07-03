from clases.Ruta import *
from clases.Router import *
from opcionesMenu import *
import random

def simularRuta(ruta: Ruta):
    cantidadRouters = random.randint(4,10)
    for i in range(cantidadRouters):
        nombreRouter = "router_" + str(i)
        router = Router(nombreRouter)
        ruta.agregarRouter(router)
    for router in ruta.routers:
        activar = random.randint(0,1)
        if activar == 1:
            router.activar()
        else:
            router.desactivar()
    mostrarRuta(ruta)