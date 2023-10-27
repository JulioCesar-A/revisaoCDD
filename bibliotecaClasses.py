class ContaBancaria:
    def __init__(self, n, num, t):
        self.NomeCliente = n
        self.NumeroConta = num
        self.TipoConta = t
        self.Limite = 0
        self.Saldo = 0
        self.StatusConta = False

    def AtivarConta(self):
        if self.StatusConta == True:
            print(f"Sua conta já está ativada")
        else:
            if self.StatusConta == False:
                print("Sua conta será ativada, por favor aguarde")
                self.StatusConta = True
                print(f"Status atual da conta: Ativa")

    def DesativarConta(self):
        if self.StatusConta == False:
            print(f"Sua conta já está desativada")
        else:
            if self.Saldo > 0:
                print(f"Por favor, retire o dinheiro da sua conta antes de desativá-la\nSaldo Atual: R${self.Saldo}")
            else:
                if self.Saldo < 0:
                    print(f"Para desativar sua conta, você deve resolver os seus débitos\nSaldo Atual: R${self.Saldo}")
                else:
                    print(f"Sua conta será desativada, por favor aguarde")
                    self.StatusConta = False
                    print(f"Status atual da conta: Inativa")

    def Sacar(self, valorSaq):
        if self.StatusConta == False:
            print(f"Operação inválida (Status atual da conta: Inativa). Primeiro ative a conta")
        else:
            if self.Limite > 0:
                if valorSaq > self.Saldo:
                    if valorSaq < self.Limite:
                        self.Saldo += self.Limite
                        self.Limite = self.Saldo - valorSaq
                        print(f"Limite atual: R${self.Limite}")
                        if self.Saldo <= 0 or self.Saldo < valorSaq:
                            print(f"Saldo insuficiente.\nSaldo Disponível: R${self.Saldo}")
                        else:
                            self.Saldo -= valorSaq
                            print(f"Valor sacado: R${valorSaq}\nSaldo atual: R${self.Saldo}")
                    else:
                        self.Saldo += self.Limite
                        print(f"ei nêga, tá querendo gastar o que não tem???????\nSaldo atual: R${self.Saldo}")
            else:
                if self.Saldo <= 0 or self.Saldo < valorSaq:
                    print(f"Saldo insuficiente.\nSaldo Disponível: R${self.Saldo}")
                else:
                    self.Saldo -= valorSaq
                    print(f"Valor sacado: R${valorSaq}\nSaldo atual: R${self.Saldo}")

    def Depositar(self, valorDep):
        if self.StatusConta == False:
            print(f"Operação inválida (Status atual da conta: Inativa). Primeiro ative a conta")
        else:
            if self.Limite
            self.Saldo += valorDep
            print(f"Valor depositado: R${valorDep}\nSaldo atual: R${self.Saldo}")

    def VerificarSaldo(self):
        if self.StatusConta == False:
            print(f"Operação inválida (Status atual da conta: Inativa). Primeiro ative a conta")
        else:
            print(f"Saldo atual: R${self.Saldo}")
    def InfoConta(self):
        print(f"Nome do Cliente: {self.NomeCliente}\nNúmero da conta: {self.NumeroConta}\nTipo da conta: {self.TipoConta}")

    def LimiteConta(self, valorLim):
        self.Limite = valorLim
        print(f"Valor do limite: R${valorLim}")