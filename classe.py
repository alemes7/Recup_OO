class Banco:
    def __init__ (self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def criar_conta(self, nome, cpf, senha, conta, saldo_inicial=0):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.conta = conta
        self.saldo_inicial = saldo_inicial

    def sacar(self, valor):
        self.valor = valor
        if valor > 0 and self.saldo_inicial >= valor:
            self.saldo_inicial -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo_inicial:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def depositar(self, valor):
        self.valor = valor  
        if valor > 0:
            self.saldo_inicial + valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo_inicial:.2f}")
        else:
            print("Valor de deposito invalido!")

    def tranferir(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor:.2f} para {destino.cliente.nome} realizada.")
        else:
            print("Valor de transferência inválido ou saldo insuficiente.")

    def saldo(self, conta):
        self.conta = conta
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R${self.saldo_inicial:.2f}")

    def getSaldo(self):
        return self.saldo