class AFDNumeroNatural:
    def __init__(self):
        self.estado = 0
    
    def transicion(self, caracter):
        if self.estado == 0:
            if caracter.isdigit():
                self.estado = 1
            else:
                self.estado = -1
        elif self.estado == 1:
            if not caracter.isdigit():
                self.estado = -1
    
    def aceptar(self):
        return self.estado == 1