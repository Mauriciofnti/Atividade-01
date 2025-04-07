# • Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
# ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o
# número do canal e o nível do volume permanecem dentro de faixas válidas.

class Teve():
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def mudarCanal(self, novoCanal):
        if novoCanal <= 0 or novoCanal > 100:
            print("Canal inválido")
        else:
            self.canal = novoCanal
            return (f"Sintonizado no canal: {self.canal}")
    def aumentarVolume(self, novoVolume):
        if novoVolume <= 0 or novoVolume > 100:
            print("Volume inválido")
        else:
            self.volume = novoVolume
            return (f"O volume está em: {self.volume}")
    def menuTeve(self):
        option = input(
                f"|** Olá Senhor {self.nome}...  SALDO R${self.saldo}\n"
                f"|\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Alterar Nome.               |\n"
                 "| 2 - Depositar.                  |\n"
                 "| 3 - Sacar.                      |\n"
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

novateve = Teve()
print(novateve.aumentarVolume(50))