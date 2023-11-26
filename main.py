import sys
from MiScanner import Scanner
from ASDI import ASDI

class Principal:
    existen_errores = False

    @staticmethod
    def main():
        Principal.ejecutar_prompt()

    @staticmethod
    def ejecutar_prompt():
        while True:
            try:
                linea = input(">>> ")
                if not linea:
                    break  # Presionar Ctrl + D
                Principal.ejecutar(linea)
                Principal.existen_errores = False
            except EOFError:
                break

    @staticmethod
    def ejecutar(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        
        analizador=ASDI(tokens)
        analizador.parse()
        


    @staticmethod
    def error(linea, mensaje):
        Principal.reportar(linea, "", mensaje)

    @staticmethod
    def reportar(linea, donde, mensaje):
        print(f"[linea {linea}] Error {donde}: {mensaje}")
        Principal.existen_errores = True

if __name__ == "__main__":
    Principal.main()