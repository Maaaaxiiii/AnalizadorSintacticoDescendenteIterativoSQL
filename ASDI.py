from Celda import Celda
from TipoToken import TipoToken

class ASDI:
    def __init__(self, tokens):
        self.i = 0
        self.hay_errores = False
        self.preanalisis = tokens[self.i]
        self.tokens = tokens

        # Inicialización de la tabla de 11x8
        self.tabla = [[None] * 8 for _ in range(11)]

        self.tabla[0][0] = Celda(["Q", "SELECT", "D", "FROM", "T"])
        self.tabla[1][2] = Celda(["D", "DISTINCT", "P"])
        self.tabla[1][3] = Celda(["D", "P"])
        self.tabla[1][5] = Celda(["D", "P"])
        self.tabla[2][3] = Celda(["P", "ASTERISCO"])
        self.tabla[2][5] = Celda(["P", "A"])
        self.tabla[3][5] = Celda(["A", "A2", "A1"])
        self.tabla[4][1] = Celda(["A1", "e"])
        self.tabla[4][4] = Celda(["A1", "COMA", "A"])
        self.tabla[5][5] = Celda(["A2", "IDENTIFICADOR", "A3"])
        self.tabla[6][1] = Celda(["A3", "e"])
        self.tabla[6][4] = Celda(["A3", "e"])
        self.tabla[6][6] = Celda(["A3", "PUNTO", "IDENTIFICADOR"])
        self.tabla[7][5] = Celda(["T", "T2", "T1"])
        self.tabla[8][4] = Celda(["T1", "COMA", "T"])
        self.tabla[8][7] = Celda(["T1", "e"])
        self.tabla[9][5] = Celda(["T2", "IDENTIFICADOR", "T3"])
        self.tabla[10][4] = Celda(["T3", "e"])
        self.tabla[10][5] = Celda(["T3", "IDENTIFICADOR"])
        self.tabla[10][7] = Celda(["T3", "e"])

    #mapear símbolos no terminales a índices específicos que corresponden a las filas de la tabla
    #toma como entrada un símbolo no terminal y utiliza un diccionario para devolver el índice correspondiente 
    # en la tabla. Si no se encuentra, devuelve -1.
    def buscar(self, aux):
        diccionario_indices = {"Q": 0, "D": 1, "P": 2, "A": 3, "A1": 4, "A2": 5, "A3": 6, "T": 7, "T1": 8, "T2": 9, "T3": 10}
        return diccionario_indices.get(aux, -1)
