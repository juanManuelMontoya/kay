from afd.numeroNatural import AFDNumeroNatural
from afd.numeroReal import AFDNumeroReal
from afd.identificador import AFDIdentificador
from afd.operadorAritmetico import AFDOperadorAritmetico
from afd.operadorComparacion import AFDOperadorComparacion
from afd.parentesis import AFDParentesis

class AnalizadorLexico:
    def __init__(self, codigo_fuente):
        self.codigo = codigo_fuente
        self.tokens = []
        self.posicion = 0

    def analizar(self):
        while self.posicion < len(self.codigo):
            if self.codigo[self.posicion].isspace():
                self.posicion += 1
                continue
            token, tipo = self.obtener_siguiente_token()
            if token:
                self.tokens.append((token, tipo, self.posicion))
            else:
                print(f"Error: Token no reconocido en la posición {self.posicion}")
                self.posicion += 1

    def obtener_siguiente_token(self):
        inicio = self.posicion

        # Lista de autómatas a probar
        automatas = [
            (AFDNumeroNatural(), 'NumeroNatural'),
            (AFDNumeroReal(), 'NumeroReal'),
            (AFDIdentificador(), 'Identificador'),
            (AFDOperadorAritmetico(), 'OperadorAritmetico'),
            (AFDOperadorComparacion(), 'OperadorComparacion'),
            (AFDParentesis(), 'Parentesis')
        ]

        for automata, tipo in automatas:
            while self.posicion < len(self.codigo):
                automata.transicion(self.codigo[self.posicion])
                if automata.estado == -1:
                    break
                self.posicion += 1
            if automata.aceptar():
                return self.codigo[inicio:self.posicion], tipo
            
            # Volver a la posicion inicial
            self.posicion = inicio

        return None, None

    def obtener_tokens(self):
        return self.tokens