class Grafite:
    def __init__ (self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size
    
    def __str__(self):
            return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
        
    def get_thickness (self):
        return self.__thickness
    
    def get_hardness (self):
        return self.__hardness
    
    def get_size (self):
        return self.__size
    
    def set_thickness (self, calibre: float):
        self.__thickness = calibre
    
    def set_hardness (self, dureza: float):
        self.__hardness = dureza

    def set_size (self, tamanho: float):
        self.__size = tamanho

    def usagePerSheet (self):
        if self.__hardness == "HB":
            self.__size -= 1
            return 1
        if self.__hardness == "2B":
            self.__size -= 2
            return 2
        if self.__hardness == "4B":
            self.__size -= 4
            return 4
        if self.__hardness == "6B":
            self.__size -= 6
            return 6
        
class Pencil:
    def __init__ (self, thickness: float):
        self.__thickness = thickness
        self.__tip = None
    
    def get_tip (self):
        return self.__tip
    
    def hasGrafite (self):
        self.__tip != None
        return True
    
    def __str__(self):
        if self.__tip == None:
            return f"calibre: {self.__thickness}, grafite: null"
        else:
            return f"calibre: {self.__thickness}, grafite: {self.__tip}"
    
    def set_thickness (self, amount: float):
        self.__thickness = amount

    def insert (self, calibre: float, dureza: str, tamanho: int):
        if calibre != self.__thickness:
            print ("fail: calibre incompativel")
            return False
        if self.__tip != None:
            print("fail: ja existe grafite")
            return False
        if calibre == self.__thickness:
            self.__tip = Grafite(calibre, dureza, tamanho)
            return True
        
    def remove (self):
        if self.__tip == None:
            print ("não tem grafite")
        else:
            self.__tip = None
        
    def write (self):
        if self.__tip == None:
            print ("fail: nao existe grafite")
            return
        
        tamanho = self.__tip.get_size()

        if tamanho == 10:
            print ("fail: tamanho insuficiente")    
            return
        
        gasto = self.__tip.usagePerSheet()
        tamanhoUsado = tamanho - gasto 

        if tamanhoUsado < 10:
            self.__tip.set_size(10)
            print ("fail: folha incompleta")
            return

def main():
    pencil = Pencil (0.00)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break 
        elif args[0] == "show":
            print (pencil)
        elif args[0] == "init":
            amount = float(args[1])
            pencil.set_thickness(amount)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            grafite = Grafite(calibre, dureza, tamanho)
            pencil.insert(calibre, dureza, tamanho)
        elif args[0] == "remove":
            pencil.remove()
        elif args[0] == "write":
            pencil.write()
        else:
            print("fail: comando inválido")

main()