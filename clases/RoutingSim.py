import asyncio

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
            if nodo.estado == "ACTIVO":
                task = asyncio.create_task(nodo.recibir_paquete(p))
                tasks.append(task)
            else:
                print("El paquete ({}) no se envió porque no esta activo el nodo de origen".format(p.contenido))
            nodo = self.ruta.head
        await asyncio.gather(*tasks)