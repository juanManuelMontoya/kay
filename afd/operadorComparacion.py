class AFDOperadorComparacion:
    def __init__(self):
        self.estado = 0

    def transicion(self, caracter):
        if self.estado == 0:
            if caracter in "<>=":
                self.estado = 1
            elif caracter == "!":
                self.estado = 2
            else:
                self.estado = -1
        elif self.estado == 1:
            if caracter == "=":
                self.estado = 3
            else:
                self.estado = -1
        elif self.estado == 2:
            if caracter == "=":
                self.estado = 3
            else:
                self.estado = -1
    
    def aceptar(self):
        return self.estado == 1 or self.estado == 3