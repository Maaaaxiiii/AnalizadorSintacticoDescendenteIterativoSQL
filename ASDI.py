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

def parse(self):
        # Inicialización de la pila
        pila = ["$", "Q"]

        #se ejecuta hasta que el tope de la pila es el símbolo de fin de entrada ($).
        while pila[-1] != "$":
        
            if pila[-1] == self.preanalisis.tipo:
                # Si el tope de la pila coincide con el tipo del token actual
                #se elimina de la pila y se avanza al siguiente token.
                pila.pop()
                self.i += 1
                self.preanalisis = self.tokens[self.i]
                #print("entre1", pila)

            elif (pila[-1] in ["SELECT", "FROM", "DISTINCT", "ASTERISCO", "PUNTO", "COMA", "IDENTIFICADOR", "PUNTO", "$"]):
                #verifica si el tope de la pila es un símbolo terminal 
                self.hay_errores = True
                #print("entre2", pila)

            elif self.tabla[self.buscar(pila[-1])][self.preanalisis.buscar()] is None:
                #verifica si la celda correspondiente en la tabla está vacía
                self.hay_errores = True
                #print("entre 3",pila)

            elif self.tabla[self.buscar(pila[-1])][self.preanalisis.buscar()] is not None:
                # significa que hay una regla gramatical definida en esa celda.
                """print(
                    f"{self.tabla[self.buscar(pila[-1])][self.preanalisis.buscar()].celda[0]}->",
                    " ".join(self.tabla[self.buscar(pila[-1])][self.preanalisis.buscar()].celda[1:]),
                )"""

                celda_actual = self.tabla[self.buscar(pila[-1])][self.preanalisis.buscar()]

                if celda_actual is not None:
                    #Se extrae la producción de la regla gramatical, 
                    # omitiendo el primer elemento que es el símbolo no terminal actual.
                    produccion = celda_actual.celda[1:]

                    #Se retira el símbolo no terminal actual de la pila.
                    #Se agrega a la pila la producción de la regla gramatical, en orden inverso. 
                    # excluyendo los epsilon.
                    pila.pop()
                    pila.extend(reversed([elem for elem in produccion if elem != "e"]))
                    #print("entre 4.1",pila)

                else:
                    self.hay_errores = True

            #print("al final",pila)

            if self.hay_errores:
                break
        

        if self.preanalisis.tipo == TipoToken.EOF and not self.hay_errores:
            print("Consulta correcta")
            return True
        else:
            print("Se encontraron errores")
        return False