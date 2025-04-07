

class MenuPrincipal():
    def __init__(self):
        self.opcao = 0

    def opcaoPrincipal(self):
        self.opcao = input("\nOlá, informe qual opcão de classe você deseja testar: \n"
                           "|---------------------------|\n"
                           "| 1 - Classe Bola.          |\n"
                           "| 2 - Classe Quadrado.      |\n"
                           "| 3 - Classe Retangulo.     |\n"
                           "| 4 - Classe Pessoa.        |\n"
                           "| 5 - Classe ContaCorrente. |\n"
                           "|---------------------------|\n"
                           )
        match int(self.opcao):
            case 1:
                from bola import Bola
                novaBola = Bola()
                novaBola.menuBola()
            case 2:
                from quadrado import Quadrado
                novoQuad = Quadrado()
                novoQuad.menuQuad()
            case 3:
                from retangulo import Retangulo
                ladoA = input("Informe o valor da base do retangulo em metros: ")
                ladoB = input("Informe o valor da altura do retangulo em metros: ")
                novoReta = Retangulo(ladoA, ladoB)
                novoReta.menuRetang()
            case 5:
                from contacorrente import ContaCorrente
                num = input("Informe o número da conta corrente: ")
                nome = input("Informe o nome do proprietário da conta: ")
                novaConta = ContaCorrente(num, nome)
                print("\n")
                novaConta.menuConta()
            case _:
                print("\n***Digite um valor válido...***\n")
                self.opcaoPrincipal()

init = MenuPrincipal()
init.opcaoPrincipal()