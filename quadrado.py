# • Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    tamanhoLado = 0

    def mudaValorDoLado(self):
        novoValor = input("Informe o novo valor do lado em cm: ")
        self.tamanhoLado = novoValor
        print(f"\n | Lado alterado para: {novoValor} cm. |\n")
    def retornaValorDoLado(self):
        print(f"\n | O valor do lado é {self.tamanhoLado} cm. |\n")
    def calculaArea(self):
        print(f"\n | A area do quadrado é de {int(self.tamanhoLado) * 4} cm. |\n")
    def menuQuad(self):
        option = input("Informe a opção desejada: \n |1 - Alterar valor do lado quadrado.\n |2 - Retorna valor do lado.\n |3 - Calcular area do quadrado. \n |0 - Voltar ao menu anterior.")
        match int(option):
            case 1:
                self.mudaValorDoLado()
                self.menuQuad()
            case 2:
                self.retornaValorDoLado()
                self.menuQuad()
            case 3:
                self.calculaArea()
                self.menuQuad()
            case 0:
                from main import MenuPrincipal
                volta = MenuPrincipal()
                volta.opcaoPrincipal()