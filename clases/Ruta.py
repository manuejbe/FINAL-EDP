import random
import time
from clases.Router import Router
import csv
from datetime import datetime
import os

class Ruta:
    def __init__(self, nombreRuta):
        self.nombreRuta = nombreRuta
        self.head = None
        self.len = 0 

    #metodo para agregar un router a la ruta
    def agregarRouter(self, router: Router):
        if self.head == None:
            self.head = router
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = router
        self.len += 1
        with open('system_log.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ROUTER_"+str(router.posicion), datetime.now(), "AGREGADO"])

    #metodo para acceder a un router de la ruta
    def accederNodo(self, numeroRouter):
        nodoActual = self.head
        while nodoActual != None:
            if nodoActual.posicion == numeroRouter:
                return nodoActual
            nodoActual = nodoActual.siguiente
        return None

    #metodo para inicializar una ruta random
    def inicializarRutaRandom (self):
        cantidadRouters = random.randint(30,45)
        for i in range(cantidadRouters):
            router = Router(i+1)
            self.agregarRouter(router)
        router = self.head
        while router != None:
            activar = random.randint(1,10)
            if activar in range(1,7):
                router.activar()
            if activar in (7,8):
                router.desactivar()
            if activar in (9,10):
                router.averiar()
            router = router.siguiente

    #metodo para crear txts vacios (1 para cada router)
    def crearTxts(self):
        carpeta = 'archivosTxts'
        for i in range(self.len):
            nombreArchivo = "router_"+str(i+1)+".txt"
            rutaArchivo = os.path.join(carpeta, nombreArchivo)
            archivo = open(rutaArchivo, "w")
            archivo.write("")
            archivo.close()

    #metodo para mostrar la ruta
    def __str__(self):
        router = self.head
        if self.len == 0:
            print("No hay routers en la ruta")
        else:
            while router != None:
                print(router)
                router = router.siguiente
        return ""
            
        
