class RoutingSim:
    def __init__(self, duracionSimulacion, ruta, paquetes):
        self.duracionSimulacion = duracionSimulacion
        self.ruta = ruta
        self.paquetes = paquetes

    async def simular(self):
        nodo = self.ruta.head
        for p in self.paquetes:
            while (nodo.posicion != p.origen):
                nodo = nodo.siguiente
            if nodo.estado == "ACTIVO":
                await nodo.recibir_paquete(p)
            else:
                print("No se envió porque no esta activo el nodo de origen")
            nodo = self.ruta.head