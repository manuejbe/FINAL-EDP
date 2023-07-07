import random

from clases.Router import Router

class Ruta:
    def __init__(self, nombreRuta):
        self.nombreRuta = nombreRuta
        self.routers = []

    def agregarRouter(self,Router: Router):
        self.routers.append(Router)

    def inicializarRutaRandom (self):
        cantidadRouters = random.randint(4,10)
        for i in range(cantidadRouters):
            nombreRouter = "router_" + str(i)
            router = Router(nombreRouter)
            self.agregarRouter(router)
        for router in self.routers:
            activar = random.randint(0,1)
            if activar == 1:
                router.activar()
            else:
                router.desactivar()