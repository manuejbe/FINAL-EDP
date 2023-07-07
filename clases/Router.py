from random import *
import time
import datetime
import csv
import auxiliares as aux
import asyncio

class Router:
    def __init__(self, posicion, estado="ACTIVO"):
        self.posicion = posicion
        self.estado = estado
        self.tiempo_reset = randint(5, 10)
        self.paquete = None
        self.tiempo_latencia = 0,1
        self.siguiente = None

    def activar(self):
        self.estado = "ACTIVO"
        aux.escribirEnLog("ACTIVADO", self.posicion)

    def desactivar(self):
        self.estado = "INACTIVO"
        aux.escribirEnLog("INACTIVO", self.posicion)



    def averiar(self):
        self.estado = "AVERIADO"

    async def recibir_paquete(self, paquete):
        self.paquete = paquete
        print(f"El paquete {self.paquete} llegó al router {self.posicion}")
        await asyncio.sleep(0.1)
        await self.enviar_paquete_siguiente()

    async def enviar_paquete_siguiente(self):
        routerActual = self
        yaPaso = False
        for i in range(self.paquete.destino-self.posicion):
            if (not yaPaso):
                if routerActual.siguiente != None:
                    match routerActual.estadoSiguiente():
                        case "ACTIVO":
                            await routerActual.siguiente.recibir_paquete(self.paquete)
                            yaPaso = True
                        case "INACTIVO":
                            routerActual = routerActual.siguiente
                        case "AVERIADO":
                            routerActual = routerActual.siguiente
                            asyncio.create_task(routerActual.reset())
                else:
                    print("El paquete llegó a destino")
                        
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