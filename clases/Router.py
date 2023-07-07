from random import *
import time

class Router:
    def _init_(self, posicion, estado="ACTIVO"):
        self.posicion = posicion
        self.estado = estado
        self.tiempo_reset = random.randint(5, 10)
        self.paquete = None
        self.tiempo_latencia = 0,1
        self.siguiente_router = None

    def activar(self):
        self.estado = "ACTIVO"
        print(f"El router en la posición {self.posicion} ha sido activado.")

    def desactivar(self):
        self.estado = "INACTIVO"
        print(f"El router en la posición {self.posicion} ha sido desactivado.")

    def averiar(self):
        self.estado = "AVERIADO"
        print(f"El router en la posición {self.posicion} ha sido averiado.")

    def recibir_paquete(self, paquete):
        self.paquete = paquete
        time.sleep(0.1)
        self.enviar_paquete_siguiente()

    def enviar_paquete_siguiente(self):
        routerActual = self
        for i in range(self.paquete.destino-self.posicion):
            if routerActual.siguiente_router != None:
                match routerActual.estadoSiguiente():
                    case "ACTIVO":
                        routerActual.siguiente_router.recibirPaquete(self.paquete)
                    case "INACTIVO":
                        routerActual = routerActual.siguiente_router
                    case "AVERIADO":
                        routerActual = routerActual.siguiente_router
                        routerActual.reset()
            else:
                print("El paquete llegó a destino")
                        
    async def reset(self):
        await time.sleep(randint(5,10))
        self.status = "ACTIVO"

    def estadoSiguiente(self):
        e = self.siguiente_router.estado
        return e
            
    def tick(self):
        if self.tiempo_latencia > 0:
            self.tiempo_latencia -= 1
        else:
            self.enviar_paquete_siguiente()