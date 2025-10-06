class Chinela: 
    def __init__ (self, tamanho: int):
        self.__tamanho = tamanho 
    
    def set_tamanho (self, numero: int) -> bool:
        if numero%2 != 0:
            print ("Numero inválido, não existe valor impar")
            return False
        if numero < 20 or numero > 50:
            print("Numero inválido")
            return False
        self.__tamanho = numero
        return True

    def get_tamanho (self):
        return self.__tamanho 

def main():
    while True:
        chinela = Chinela(0)
        numero: int = int(input("Diga o tamanho da sua chinela "))
        if chinela.set_tamanho(numero):
            print("Tamanho correto")
            break
    
main()