from TipoToken import TipoToken
from Token import Token

class Scanner:
    palabras_reservadas = {
        "select": TipoToken.SELECT,
        "from": TipoToken.FROM,
        "distinct": TipoToken.DISTINCT,
    }

    def __init__(self, source):
        self.source = source + " "
        self.tokens = []

    def scan_tokens(self):
        estado = 0
        lexema = ""
        i=0
        inicio_lexema = 0

        while i < len(self.source):
            caracter = self.source[i]

            if estado == 0:
                if caracter == '*':
                    self.tokens.append(Token(TipoToken.ASTERISCO, "*", i + 1))
                elif caracter == ',':
                    self.tokens.append(Token(TipoToken.COMA, ",", i + 1))
                elif caracter == '.':
                    self.tokens.append(Token(TipoToken.PUNTO, ".", i + 1))
                elif caracter.isalpha():
                    estado = 1
                    lexema += caracter
                    inicio_lexema = i
            elif estado == 1:
                if caracter.isalpha() or caracter.isdigit():
                    lexema += caracter
                else:
                    tt = Scanner.palabras_reservadas.get(lexema)
                    if tt is None:
                        self.tokens.append(Token(TipoToken.IDENTIFICADOR, lexema, inicio_lexema + 1))
                    else:
                        self.tokens.append(Token(tt, lexema, inicio_lexema + 1))

                    estado = 0
                    i -= 1
                    lexema = ""
                    inicio_lexema = 0
            i += 1  

        self.tokens.append(Token(TipoToken.EOF, "", len(self.source)))

        return self.tokens
