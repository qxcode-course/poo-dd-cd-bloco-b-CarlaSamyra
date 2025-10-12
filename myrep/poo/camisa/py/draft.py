class Camisa:
    def __init__ (self, tamanho: str):
        self.__tamanho = tamanho

    def get_tamanho (self):
        return self.__tamanho
    
    def set_tamanho (self, numero: str):
        if numero != "PP" and numero != "P" and numero != "M" and numero != "G" and numero != "GG" and numero != "XG":
            print("Tamanho de roupa inválido! Valores permitidos: PP, P, M, G, GG e XG")
            return False
        else:
            print ("Tamanho de roupa válido!")
            return True

def main():
    while True:
        camisa = Camisa("")
        line: str = (input("Informe o tamanho da sua camisa: "))
        if camisa.set_tamanho(line):
            break
main() 
