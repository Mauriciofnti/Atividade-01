# • Classe Retangulo: Crie uma classe que modele um retangulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
# de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
# de rodapés necessárias para o local.

class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.area = int(ladoA) * int(ladoB)
        self.perimetro = (int(ladoA) * 2) + (int(ladoB) * 2)

    def mudaValorLado(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB
        self.retornaValorLados()
        
    def retornaValorLados(self):
        print(f"\nO valor dos lados é: \nBase: {self.ladoA}m, \nAltura: {self.ladoB}m.\n")
        
    def calculaArea(self):
        print(f"\nO valor da área desse retangulo é {self.area}m².\n")
        
    def calculaPeri(self):
        print(f"\nO perimetro do retangulo é {(int(self.ladoA) + int(self.ladoB)) * 2}m.\n")
        
    def calcularPisos(self):
        pisos = self.area / 0.25
        rodapes = self.perimetro / 0.15
        print(
                f"\nConsiderando pisos de 50x50 cm serão necessários no minimo {int(pisos)} pisos para preencher uma área de {self.area} m²,"
                f"e {rodapes:.2f} rodapés de 15 cm cada.\n"
              )
    
    def menuRetang(self):
        option = input(
                        "|** Informe a opção desejada:                  |\n"
                        "| 1 - Alterar valor do lado retangulo.         |\n"
                        "| 2 - Retorna valor do lado.                   |\n"
                        "| 3 - Calcular área do retangulo.              |\n"
                        "| 4 - Calcular perimetro do retangulo.         |\n"
                        "| 5 - Calcular quantidade de pisos e rodapés.  |\n"
                        "| 0 - Voltar ao menu anterior.                 |\n"
                       )
        match int(option):
            case 1:
                ladoA = int(input("Informe o novo valor da base do retangulo em metros: "))
                ladoB = int(input("Informe a novo valor da altura do retangulo em metros: "))
                self.mudaValorLado(ladoA, ladoB)
                self.menuRetang()
            case 2:
                self.retornaValorLados()
                self.menuRetang()
            case 3:
                self.calculaArea()
                self.menuRetang()
            case 4:
                self.calculaPeri()
                self.menuRetang()
            case 5:
                self.calcularPisos()
                self.menuRetang()
            case 0:
                from main import MenuPrincipal
                volta = MenuPrincipal()
                volta.opcaoPrincipal()

# ladoA = int(input("Informe a media do Lado A: "))
# ladoB = int(input("Informe a media do Lado B: "))
# local = Retangulo(ladoA, ladoB)

# print(f"A área é: {local.calculaArea()}\nO perimetro é: {local.calculaPeri()}")