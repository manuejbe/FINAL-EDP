from random import *
import time
from datetime import datetime
import csv
import auxiliares as aux
import asyncio
from clases.Cola import Cola
##un router puede tener muchos paquetes, tiene que tener una lista de paquetes y que lo appendee
##hay que hacer que se borre el paquete si no es el nodo de origen
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

    def activar(self):
        self.estado = "ACTIVO"
        aux.escribirEnLog("ACTIVADO", self.posicion)

    def desactivar(self):
        self.estado = "INACTIVO"
        aux.escribirEnLog("INACTIVO", self.posicion)



    def averiar(self):
        self.estado = "AVERIADO"

    async def recibir_paquete(self, paquete):
        if paquete.destino != self.posicion and paquete.origen != self.posicion:
            print(f"El paquete ({paquete.contenido}) llegó al router {self.posicion}", datetime.now())
            self.paquetesRetrans.encolar(paquete)

        if paquete.origen == self.posicion:
            print(f"El paquete ({paquete.contenido}) se originó en el router {self.posicion}", datetime.now())
            self.paquetesOriginados.encolar(paquete)

        if paquete.destino == self.posicion:
            print(f"El paquete ({paquete.contenido}) llegó a su destino", datetime.now())
            self.paquetesDestinados.append(paquete)
        
        while not self.paquetesRetrans.esta_vacia():
            if (not self.paquetesRetrans.esta_vacia()):
                await self.enviar_paquete_siguiente(self.paquetesRetrans.desencolar())
        for i in range(self.paquetesOriginados.tamano()):
            await self.enviar_paquete_siguiente(self.paquetesOriginados.desencolar())
                


        

    async def enviar_paquete_siguiente(self, paquete):
        await asyncio.sleep(0.1)
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
                     
    async def reset(self):
        aux.escribirEnLog("EN_RESET", self.posicion)
        await asyncio.sleep(randint(5,10))
        self.activar()

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