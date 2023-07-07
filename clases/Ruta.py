import random
import time
from clases.Router import Router
import csv
from datetime import datetime

class Ruta:
    def __init__(self, nombreRuta):
        self.nombreRuta = nombreRuta
        self.head = None
        self.len = 0 

    def agregarRouter(self, router: Router):
        if self.head == None:
            self.head = router
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = router
        self.len += 1
        with open('system_log.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ROUTER_"+router.posicion, datetime.now(), "AGREGADO"])

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

    def __str__(self):
        router = self.head
        if self.len == 0:
            print("No hay routers en la ruta")
        else:
            while router.siguiente != None:
                print(router)
                router = router.siguiente
            
        
