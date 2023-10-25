#comendo=False
class Pessoa:
    def __init__(self, N, I, P,C=False, D=False, A=False):
        self.nome = N
        self.idade = I
        self.peso = P
        self.comendo = C
        self.dormindo = D
        self.andando = A
    def comer(self, alimento):
        if self.andando == True:
            print(f"{self.nome} está andando")
        else:
            if self.dormindo == True:
                print(f"{self.nome} está dormindo")
            else:
                if self.comendo == False:
                    self.alimento = alimento
                    self.comendo = True
                    print(f"{self.nome} foi comer {self.alimento}")
                else:
                    print(f"{self.nome} já está comendo")
    def parar_comer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"Não está comendo")
    def andar(self):
        self.andando = True
        print(f"{self.nome} andou...")
    def parar_andar(self):
        if self.andando == True:
            print(f"{self.nome} parou de andar")
        else:
            print(f"Não está andando")
    def dormir(self):
        self.dormindo = True
        print(f"{self.nome} dormiu...")
    def acordou(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou")
        else:
            print(f"{self.nome} já está acordado(a)")

p1 = Pessoa("Ranna", 19,49)
print(p1.nome, p1.idade, p1.peso)
p1.comer("Feijão")
p1.comer("Arroz")
#p1.parar_comer()
#p1.andar()
#p1.parar_andar()
#p1.dormir()
#p1.acordou()

p2 = Pessoa