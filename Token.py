from TipoToken import TipoToken

class Token:
    def __init__(self, tipo, lexema, posicion):
        self.tipo = tipo
        self.lexema = lexema
        self.posicion = posicion

    def buscar(self):
        tipo_indices = {
            "SELECT": 0,
            "FROM": 1,
            "DISTINCT": 2,
            "ASTERISCO": 3,
            "COMA": 4,
            "IDENTIFICADOR": 5,
            "PUNTO": 6,
            "EOF": 7
        }

        return tipo_indices.get(self.tipo, -1)


    def __eq__(self, other):
        if not isinstance(other, Token):
            return False

        return self.tipo == other.tipo
