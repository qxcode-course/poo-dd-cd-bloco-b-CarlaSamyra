class Passageiro:
    def __init__ (self, name: str, money: int):
        self.__name = name 
        self.__money = money 
    
    def get_name (self):
        return self.__name 
    
    def get_money (self):
        return self.__money 
    
    def __str__ (self):
        return f"{self.__name}:{self.__money}"

class Motorista:
    def __init__ (self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro
    
    def get_nome (self):
        return self.__nome 
    
    def get_dinheiro (self):
        return self.__dinheiro
    
    def __str__ (self):
        return f"{self.__nome}:{self.__dinheiro}"

class Moto:
    def __init__ (self, custo: int, driver: str, passager: str):
        self.__custo = custo 
        self.__driver = None
        self.__passager = None
    
    def __str__ (self):
        return f"Cost: {self.__custo}, Driver: {self.__driver}, Passenger: {self.__passager}"
    
    def set_driver (self, motorista: Motorista):
            self.__driver = motorista 
            return True
    
    def set_pass (self, passageiro: Passageiro):
            self.__passager = passageiro
            return True
    
    def drive (self, amount: int):
        self.__custo = amount

def main():
    moto = Moto (0, "", "")
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break 
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            motorista = Motorista (nome, dinheiro)
            moto.set_driver(motorista)
        elif args[0] == "setPass":
            name = args[1]
            money = int(args[2])
            passageiro = Passageiro (name, money)
            moto.set_pass(passageiro)
        elif args[0] == "drive":
            amount: int = int(args[1])
            moto.drive(amount)
        else:
            print("fail: comando inválido")

main()