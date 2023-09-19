from classe import *
import time
import os

def espera():
    time.sleep(1)

def main():
    clientes = []
    sair = False
    while sair == False:
        os.system("cls")
        print("Bem vindo ao Software Bancario!")
        escolha = int(input("Escolha a opção que deseja:\n[1] Cadastro\n[2] Fazer login\n[3] Sair: "))
        match escolha:
            case 1:
                os.system("cls")
                nome = input("Nome: ")
                cpf = input("CPF: ")
                senha = input("Senha: ")
                novo_cliente = Banco(nome, cpf, senha)
                clientes.append(novo_cliente)
                print("Cliente cadastrado com sucesso!")
                espera()
                
            case 2:
                os.system("cls")
                cpf = input("CPF: ")
                senha = input("Senha: ")
                
                cliente_logado = None
                for cliente in clientes:
                    if cliente.cpf == cpf and cliente.senha == senha:
                        cliente_logado = cliente
                        break
                
                if cliente_logado:
                    os.system("cls")
                    print(f"Bem-vindo, {cliente_logado.nome}!")

                    while True:
                        print("Menu do Cliente:")
                        opção = int(input("Digite a opção que deseja:\n[1] Sacar\n[2] Depositar\n[3] Transferir\n[4] Ver Saldo\n[5] Logout: "))
                        match opção:
                            case 1:
                                os.system("cls")
                                print("Você escolheu sacar.")
                                valor = float(input("Digite o valor do saque: "))
                                cliente_logado.sacar(valor)
                                print("Saque concluido")

                            case 2:
                                os.system("cls")
                                print("Você escolheu depositar.")
                                cliente_logado.depositar(valor)

                            case 3:
                                os.system("cls")
                                print("Você escolheu tranferir.")
                                cpf_destinatario = input("Digite o CPF do destinatário: ")
                                valor = float(input("Digite o valor para transferência: R$"))

                                destinatario = None
                                for cliente in clientes:
                                    if cliente.cpf == cpf_destinatario:
                                        destinatario = cliente
                                        break

                                if destinatario:
                                    cliente_logado.transferir(destinatario, valor)
                                else:
                                    print("Destinatário não encontrado.")

                            case 4:
                                pass

                            case 5:
                                os.system("cls")
                                print("Fazendo logout...")
                                espera()
                                break
            case 3:
                print("Saindo do software...")
                espera()
                sair = True

            case _:
                print("Valor invalido!")