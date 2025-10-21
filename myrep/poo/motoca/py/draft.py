class Pessoa:
    def __init__ (self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __str__ (self):
        return f"{self.__name}:{self.__age}"
    
    def get_name (self):
        return self.__name
    
    def get_age (self):
        return self.__age

class Moto:
    def __init__ (self, person: str, potencia: int, tempo: int):
        self.__person = None
        self.__potencia = 1
        self.__tempo = 0 
    
    def __str__ (self):
        st = f"power:{self.__potencia}, time:{self.__tempo}, "
        if self.__person == None:
            st += f"person:(empty)"
        else:
            st += f"person:({self.__person})"
        return st
    
    def enter (self, pessoa: Pessoa):
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        self.__person = pessoa
        return True
    
    def init (self, init: int):
        self.__potencia = init
        return self.__potencia
    
    def leave (self):
        if self.__person != None:
            print(self.__person)
            self.__person = None
        else:
            print ("fail: empty motorcycle")
        
    def buy (self, buy: int):
        self.__tempo += buy
        return self.__tempo
    
    def drive (self, amount: int):
        if self.__tempo == 0:
            print ("fail: buy time first")
            return
        if self.__person == None:
            print("fail: empty motorcycle")
            return
        if self.__person.get_age() > 10:
            print ("fail: too old to drive")
            return
        if amount > self.__tempo:
            print (f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0
            return
        self.__tempo -= amount

    def honk (self):
        buzina = "P" + ("e" * self.__potencia) + "m"
        return buzina


def main():
    moto = Moto ("", 1, 0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa (nome, idade)
            moto.enter(pessoa)
        elif args[0] == "init":
            init = int(args[1])
            moto.init(init)
        elif args[0] == "leave":
            moto.leave()
        elif args[0] == "buy":
            buy = int(args[1])
            moto.buy(buy)
        elif args[0] == "drive":
            amount: int = int(args[1])
            moto.drive(amount)
        elif args[0] == "honk":
            print(moto.honk())
        else:
            print("fail: comando inválido")

main()
