

class MenuPrincipal():
    def __init__(self):
        self.opcao = 0

    def opcaoPrincipal(self):
        self.opcao = input("\nOlá, informe qual opcão de classe você deseja testar: \n"
                           "|-----------------------------------|\n"
                           "| 1 - Classe Bola.                  |\n"
                           "| 2 - Classe Quadrado.              |\n"
                           "| 3 - Classe Retangulo.             |\n"
                           "| 4 - Classe Pessoa(off).           |\n"
                           "| 5 - Classe ContaCorrente.         |\n"
                           "| 6 - Classe Teve.                  |\n"
                           "| 7 - Classe Tamagushi.             |\n"
                           "| 8 - Classe Macaco(off).           |\n"
                           "| 9 - Classe Ponto(off).            |\n"
                           "| 10 - Classe Posto de Combustível. |\n"
                           "|-----------------------------------|\n"
                           )
        match int(self.opcao):
            case 1:
                from classes.bola import Bola
                novaBola = Bola()
                novaBola.menuBola()
            case 2:
                from classes.quadrado import Quadrado
                novoQuad = Quadrado()
                novoQuad.menuQuad()
            case 3:
                from classes.retangulo import Retangulo
                ladoA = input("Informe o valor da base do retangulo em metros: ")
                ladoB = input("Informe o valor da altura do retangulo em metros: ")
                novoReta = Retangulo(ladoA, ladoB)
                novoReta.menuRetang()
            case 5:
                from classes.contacorrente import ContaCorrente
                num = input("Informe o número da conta corrente: ")
                nome = input("Informe o nome do proprietário da conta: ")
                novaConta = ContaCorrente(num, nome)
                print("\n")
                novaConta.menuConta()
            case 6:
                from classes.teve import Teve
                novaTeve = Teve()
                novaTeve.menuTeve()
            case 7:
                from classes.tamagushi import Tamagushi
                nome = input("Informe o nome do Tamagushi: ")
                novoTama = Tamagushi(nome)
                novoTama.menuTama()
            case 10:
                from classes.postocombustivel import BombaCombustivel
                novaBomba = BombaCombustivel()
                novaBomba.menuPosto()
            case 00:
                from init import Init
                Init().opcaoPrincipal()
            case _:
                print("\n***Digite um valor válido...***\n")
                self.opcaoPrincipal()