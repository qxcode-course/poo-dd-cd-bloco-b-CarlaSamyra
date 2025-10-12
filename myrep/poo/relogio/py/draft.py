class Relogio:
    def __init__ (self, hora: int, minuto: int, segundo: int):
        self.__hora = int(hora) 
        self.__minuto = int(minuto)
        self.__segundo = int(segundo) 

    def __str__ (self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
    
    def get_hora (self):
        return self.__hora
    
    def get_minuto (self):
        return self.__minuto
    
    def get_segundo (self):
        return self.__segundo
    
    def set_hora (self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
        else:
            self.__hora = int(hora)
        
    def set_minuto (self, minuto: int):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
        else:
            self.__minuto = int(minuto)
        
    def set_segundo (self, segundo: int):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
        else:
            self.__segundo = int(segundo)
    
    def set_horainit (self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            self.__hora = 0 
        else:
            self.__hora = int(hora)
        
    def set_minutoinit (self, minuto: int):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
            self.__minuto = 0 
        else:
            self.__minuto = int(minuto)
        
    def set_segundoinit (self, segundo: int):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
            self.__segundo = 0 
        else:
            self.__segundo = int(segundo)
    
    def nextSecond (self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto == 60:
            self.__minuto = 0
            if self.__hora < 23:
                self.__hora += 1
        if self.__hora == 23:
            self.__hora = 0

def main():
    relogio = Relogio (0, 0, 0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break 
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.set_hora(hora)
            relogio.set_minuto(minuto)
            relogio.set_segundo(segundo)
        elif args[0] == "next":
            relogio.nextSecond()
        elif args[0] == "init":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.set_horainit(hora)
            relogio.set_minutoinit(minuto)
            relogio.set_segundoinit(segundo)
        else:
            print("fail: comando inválido")
main()