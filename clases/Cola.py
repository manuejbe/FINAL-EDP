class Cola:
    def __init__(self):
        self.cola = []

    #metodo para saber si la cola esta vacia
    def esta_vacia(self):
        return len(self.cola) == 0

    #metodo para encolar un elemento a la cola
    def encolar(self, elemento):
        self.cola.append(elemento)

    #metodo para desencolar un elemento de la cola
    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.cola.pop(0)
        
    #metodo para ver el primer elemento de la cola
    def ver_primero(self):
        if self.esta_vacia():
            raise IndexError("No se puede mirar el primer elemento de una cola vacía")
        return self.cola[0]

    #metodo para ver el tamano de la cola
    def tamano(self):
        return len(self.cola)