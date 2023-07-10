from random import *
import time
from datetime import datetime
import csv
import auxiliares as aux
import asyncio
from clases.Cola import Cola
import os

class Router:
    def __init__(self, posicion, estado="ACTIVO"):
        self.posicion = posicion
        self.estado = estado
        self.tiempo_reset = randint(5, 10)
        self.paquete = None
        self.tiempo_latencia = 0,1
        self.siguiente = None
        self.paquetesRetrans = Cola() #paquetes que se retransmiten
        self.paquetesOriginados = Cola() #paquetes que se originan en este router
        self.paquetesDestinados = [] #paquetes que se quedan en este router
        self.paquetesRecibidos = 0
        self.contPaquetesOriginados = 0

    #metodo para activar el router
    def activar(self):
        self.estado = "ACTIVO"
        aux.escribirEnLog("ACTIVADO", self.posicion)

    #metodo para desactivar el router
    def desactivar(self):
        self.estado = "INACTIVO"
        aux.escribirEnLog("INACTIVO", self.posicion)

    #metodo para averiar el router (se usa al crearse una ruta aleatoria)
    def averiar(self):
        self.estado = "AVERIADO"

    #metodo para recibir el paquete
    async def recibir_paquete(self, paquete):
        self.paquetesRecibidos += 1
        #chequea si el paquete no tiene como destino u origen el router actual
        if paquete.destino != self.posicion and paquete.origen != self.posicion:
            print(f"El paquete ({paquete.contenido}) llegó al router {self.posicion}", datetime.now())
            self.paquetesRetrans.encolar(paquete)
        #chequea si el paquete tiene como origen el router actual
        if paquete.origen == self.posicion:
            print(f"El paquete ({paquete.contenido}) se originó en el router {self.posicion}", datetime.now())
            self.paquetesOriginados.encolar(paquete)
        #chequea si el paquete tiene como destino el router actual
        if paquete.destino == self.posicion:
            print(f"El paquete ({paquete.contenido}) llegó a su destino", datetime.now())
            self.paquetesDestinados.append(paquete)
            nombreArchivo="router_"+str(self.posicion)+".txt"
            carpeta = 'archivosTxts'
            rutaArchivo = os.path.join(carpeta, nombreArchivo)
            with open(rutaArchivo, 'a') as file:
                file.write("Origen: ROUTER_"+str(paquete.origen))
                file.write('\n')
                file.write(paquete.contenido)
                file.write('\n')
                

        #validacion para otorgarle prioridad a los paquetes que tiene que retransmitir el router por sobre los originados en el
        while not self.paquetesRetrans.esta_vacia():
            if (not self.paquetesRetrans.esta_vacia()):
                await self.enviar_paquete_siguiente(self.paquetesRetrans.desencolar())
        for i in range(self.paquetesOriginados.tamano()):
            self.contPaquetesOriginados += 1
            self.paquetesRecibidos -= 1
            await self.enviar_paquete_siguiente(self.paquetesOriginados.desencolar())

    #metodo para enviar el paquete al siguiente router         
    async def enviar_paquete_siguiente(self, paquete):
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            return
        routerActual = self
        yaPaso = False
        for i in range(paquete.destino-self.posicion):
            if (not yaPaso):
                if routerActual.siguiente != None:
                    match routerActual.estadoSiguiente():
                        case "ACTIVO":
                            await routerActual.siguiente.recibir_paquete(paquete)
                            yaPaso = True
                        case "INACTIVO":
                            routerActual = routerActual.siguiente
                        case "AVERIADO":
                            routerActual = routerActual.siguiente
                            asyncio.create_task(routerActual.reset())

    #metodo para resetear el router         
    async def reset(self):
        aux.escribirEnLog("EN_RESET", self.posicion)
        await asyncio.sleep(randint(5,10))
        self.activar()

    #metodo para obtener el estado del router siguiente
    def estadoSiguiente(self):
        e = self.siguiente.estado
        return e
    

    def tick(self):
        if self.tiempo_latencia > 0:
            self.tiempo_latencia -= 1
        else:
            self.enviar_paquete_siguiente()

    def __str__(self):
        return f"Router {self.posicion}: {self.estado}"