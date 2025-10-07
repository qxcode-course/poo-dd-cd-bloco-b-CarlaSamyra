class Roupa:
    def __init__ (self, tamanho: str):
        self.__tamanho: str = tamanho 

    def __str__ (self):
        return f"size: ({self.__tamanho})"
    
    def get_tamanho (self):
        return self.__tamanho
    
    def set_tamanho (self, numero: str) -> bool:
        if numero != "PP" and numero != "P" and numero != "M" and numero != "G" and numero != "GG" and numero != "XG":
            print ("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return False
        else:
            self.__tamanho = numero 
            return True
    
def main():
    roupa = Roupa("")
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            numero: str = str(args[1])
            roupa.set_tamanho(numero)
        else: 
            print("fail: comando invalido")
main()