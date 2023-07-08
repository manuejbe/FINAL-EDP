class Cola:
    def __init__(self):
        self.cola = []

    def esta_vacia(self):
        return len(self.cola) == 0

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.cola.pop(0)
        
    
    def ver_primero(self):
        if self.esta_vacia():
            raise IndexError("No se puede mirar el primer elemento de una cola vacía")
        return self.cola[0]

    def tamano(self):
        return len(self.cola)