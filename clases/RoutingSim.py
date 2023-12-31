import asyncio
from auxiliares import *

class RoutingSim:
    def __init__(self, duracionSimulacion, ruta, paquetes):
        self.duracionSimulacion = duracionSimulacion
        self.ruta = ruta
        self.paquetes = paquetes


    async def simular(self):
        nodo = self.ruta.head
        tasks = []
        for p in self.paquetes:
            while (nodo.posicion != p.origen):
                nodo = nodo.siguiente
            #chequea si el nodo de origen esta activo porque sino no puede comenzar el envio del paquete
            if nodo.estado == "ACTIVO":
                task = asyncio.create_task(nodo.recibir_paquete(p))
                tasks.append(task)
            else:
                print("El paquete ({}) no se envió porque no esta activo el nodo de origen".format(p.contenido))
            nodo = self.ruta.head
        d= asyncio.create_task(self.duracion(tasks))
        await asyncio.gather(*tasks, d)

        await asyncio.sleep(10)

    async def duracion(self, tasks):
        estados = []
        for i in range(len(tasks)):
            estados.append(False)
        for i in range(self.duracionSimulacion*10-1):
            if verificarArrayTrue(estados) == False:
                for i in range(len(tasks)):
                    estados[i] = tasks[i].done()
                await asyncio.sleep(0.1)

        if not verificarArrayTrue(estados):
            for i in range(len(tasks)):
                if not tasks[i].done(): 
                    tasks[i].cancel()
            print("* * * \n LA SIMULACION HA TERMINADO ABRUPTAMENTE, SE HA SUPERADO EL TIEMPO DE SIMULACION\n* * *")
        else:
            print("* * * \n LA SIMULACION TOMO MENOS TIEMPO DEL INGRESADO.\n* * *")