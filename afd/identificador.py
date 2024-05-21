class AFDIdentificador:
    def __init__(self):
        self.estado = 0
        self.longitud = 0
    
    def transicion(self, caracter):
        if self.estado == 0:
            if caracter.isalpha() or caracter == '_':
                self.estado = 1
                self.longitud += 1
            else:
                self.estado = -1
        elif self.estado == 1:
            if caracter.isalnum() or caracter == '_':
                self.longitud += 1
                if self.longitud > 10:
                    self.estado = -1
            else:
                self.estado = -1
    
    def aceptar(self):
        return self.estado == 1