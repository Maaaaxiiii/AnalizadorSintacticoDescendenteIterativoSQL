from Celda import Celda
from TipoToken import TipoToken

class ASDI:
    def __init__(self, tokens):
        self.i = 0
        self.hay_errores = False
        self.preanalisis = tokens[self.i]
        self.tokens = tokens
        