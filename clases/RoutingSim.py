class RoutingSim:
    def __init__(self, duracionSimulacion, ruta, paquetes):
        self.duracionSimulacion = duracionSimulacion
        self.ruta = ruta
        self.paquetes = paquetes

    async def simular(self):
        for p in self.paquetes:
            await self.ruta.head.recibir_paquete(p)