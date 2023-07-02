class Router:
    def __init__(self, nombre, status: bool = True):
        self.nombre = nombre
        self.status = status

    def activar(self):
        self.status = True

    def desactivar(self):
        self.status = False
    
    def __str__(self):
        return f'Nombre de router: ${self.nombre}'