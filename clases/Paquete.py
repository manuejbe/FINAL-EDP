class Paquete:
    def _init_(self, origen, destino, contenido):
        self.origen = origen
        self.destino = destino
        self.contenido = contenido
        self.en_ruta = False

    def enviar(self):
        print(f"Enviando paquete de {self.origen} a {self.destino}...")
        self.en_ruta = True

    def recibir(self):
        print(f"Paquete recibido en {self.destino}.")

    def _str_(self):
        return f"Paquete de {self.origen} a {self.destino}"