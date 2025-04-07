# • Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
# seguintes: alterarNome, depósito e saque. No construtor, saldo é opcional, com valor default zero e os
# demais atributos são obrigatórios.

class ContaCorrente():
    def __init__(self, numConta, nome, saldo=0):
        self.numConta = numConta
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    
    def deposito(self, valor):
        self.saldo += int(valor)
        return self.saldo
    
    def saque(self, valor):
        self.saldo -= int(valor)
        return self.saldo
    
    def menuConta(self):
        option = input(
                f"|** Olá Senhor {self.nome}...  SALDO R${self.saldo}\n"
                f"|\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Alterar Nome.               |\n"
                 "| 2 - Depositar.                  |\n"
                 "| 3 - Sacar.                      |\n"
                 "| 0 - Sair.                       |\n"
                )
        match int(option):
            case 1:
                novoNome = input("Informe o novo nome: ")
                self.alterarNome(novoNome)
                self.menuConta()
            case 2:
                valor = input("Informe o valor a ser depositado: ")
                self.deposito(valor)
                print(f"O deposito no valor de R${valor} foi efetuado com sucesso, seu novo saldo é de R${self.saldo}.\n")
                self.menuConta()
            case 3:
                valor = input("Informe o valor a ser sacado: ")
                if float(valor) > self.saldo:
                    print("Seu saldo não é suficiente..")
                    self.menuConta()
                else:
                    self.saque(valor)
                    print(f"O saque no valor de R${valor} foi efetuado com sucesso, seu novo saldo é de R${self.saldo}.\n")
                    self.menuConta()
            case 0:
                from main import MenuPrincipal
                volta = MenuPrincipal()
                volta.opcaoPrincipal()