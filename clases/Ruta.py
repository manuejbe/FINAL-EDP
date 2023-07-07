import random
import time
from clases.Router import Router

class Ruta:
    def _init_(self, nombreRuta):
        self.nombreRuta = nombreRuta
        self.head = None

    def agregarRouter(self,Router: Router):
        if self.head == None:
            self.head = Router
        else:
            self.head.siguiente = Router

    def accederNodo(self, numeroRouter):
        nodoActual = self.head
        while nodoActual != None:
            if nodoActual.numero == numeroRouter:
                return nodoActual
            nodoActual = nodoActual.siguiente
        return None
    
    def moverPaquete(self, numeroRouter):
        routerOrigen = self.accederNodo(numeroRouter)
        for i in range(routerOrigen.paquete.origen,routerOrigen.paquete.destino):
            routerActual = self.accederNodo(i)
            if self.accederNodo(i).status == True:
                time.sleep(0.1)


    def inicializarRutaRandom (self):
        cantidadRouters = random.randint(4,10)
        for i in range(cantidadRouters):
            nombreRouter = "router_" + str(i)
            router = Router(nombreRouter)
            self.agregarRouter(router)
        for router in self.routers:
            activar = random.randint(0,2)
            if activar == 1:
                router.activar()
            if activar == 2:
                router.desactivar()
            if activar == 3:
                router.averiar()