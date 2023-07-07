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
            await nodo.recibir_paquete(p)
            nodo = self.ruta.head