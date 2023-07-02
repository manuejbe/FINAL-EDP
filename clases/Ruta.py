from clases.Router import Router

class Ruta:
    def __init__(self, nombreRuta):
        self.nombreRuta = nombreRuta
        self.routers = []

    def agregarRouter(self,Router: Router):
        self.routers.append(Router)