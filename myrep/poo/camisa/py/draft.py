class Camisa:
    def __init__ (self, tamanho: str):
        self.__tamanho = tamanho

    def get_tamanho (self):
        return self.__tamanho
    
    def set_tamanho (self, numero: str):
        if numero == "PP" or numero == "P" or numero == "M" or numero == "G" or numero == "GG" or numero == "XG":
            print("Tamanho de roupa válido!")
            return True
        else:
            print ("Tamanho de roupa inválido! Valores permitidos: PP, P, M, G, GG e XG")
            return False

def main():
    while True:
        camisa = Camisa("")
        line: str = (input("Informe o tamanho da sua camisa: "))
        if camisa.set_tamanho(line):
            break
main() 
