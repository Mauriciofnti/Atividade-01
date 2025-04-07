# • Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor
from bola import NovaBola

opcao = input("Olá, informe qual opcão de classe você deseja testar: ")

match opcao:
    case 1:
        NovaBola()

class Bola():
    cor = ''
    circunferencia = ''
    material =''

    def trocaCor(self, novaCor): 
        self.cor = novaCor
    def mostraCor(self):
        print(f"Cor da bola: {self.cor}")

bola1 = Bola()
bola1.trocaCor("Azul")
bola1.mostraCor()

# • Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    tamanhoLado = 0

    def mudaValorDoLado(self, novoValor):
        self.tamanhoLado = novoValor
    def retornaValorDoLado(self):
        print(f"O valor do lado é: {self.tamanhoLado}")
    def calculaArea(self):
        return self.tamanhoLado * 4

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

    def mudaValorLado(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB
    def retornaValorLados(self):
        print(f"O valor dos lado é: \nLadoA: {self.ladoA}, \nLadoB: {self.ladoB}")
    def calculaArea(self):
        return self.ladoA * self.ladoB
    def calculaPeri(self):
        return (self.ladoA + self.ladoB) * 2

# ladoA = int(input("Informe a media do Lado A: "))
# ladoB = int(input("Informe a media do Lado B: "))
# local = Retangulo(ladoA, ladoB)

# print(f"A aréa é: {local.calculaArea()}\nO perimetro é: {local.calculaPeri()}")

# • Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: envelhecer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
# ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        anosAntes = self.idade
        self.idade += anos
        if (anosAntes < 25):
            if (self.idade < 25):
                self.crescer(anos * 0.5)
            else:
                self.crescer((25 - anosAntes) + 0.5)
    def engordar(self, peso):
        novoPeso = peso


# • Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
# seguintes: alterarNome, depósito e saque. No construtor, saldo é opcional, com valor default zero e os
# demais atributos são obrigatórios.

class ContaCorrente():
    def __init__(self, numConta, nome, saldo):
        self.numConta = numConta
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
        return novoNome
    def deposito(self, valor):
        self.saldo += valor
        return self.saldo
    def saque(self, valor):
        self.saldo -= valor
        return self.saldo
    
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

novateve = Teve()
print(novateve.aumentarVolume(50))

# • Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
# este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então
# não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a
# qualquer momento.
    

class Tamagushi():
    def __init__(self):
        self.nome = "Tamagushi"
        self.fome = 10
        self.saude = 10
        self.idade = 0

    def alterarNome(self, newName):
        self.nome = newName
    def aumentaFome(self):
        if self.fome <= 0:
            print("Morto!!!")
        else:           
            self.fome -= 1
    def retornaNome(self):
        return self.nome
    def retornaFome(self):
        return self.fome
    def retornaSaude(self):
        return self.saude
    def retornaIdade(self):
        return self.idade
    def retornaHumor(self):
        return self.humor()
    def humor(self):
        if self.fome <= 3 or self.saude <= 3:
            return ("Infeliz")
        elif self.fome <= 6 or self.saude <= 6:
            return ("Sem humor")
        elif self.fome <= 8 or self.saude <= 8:
            return ("Feliz")
        else:
            return ("Muito feliz")
tama = Tamagushi()
print(tama.retornaSaude())

# • Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago)
# e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
# criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
# verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o
# outro. É possível criar um macaco canibal?

class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, comida):
        self.bucho.append(comida)
        return print(self.verBucho())
    
    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho.pop()

macaco1 = Macaco("bob")
macaco1.comer("banana")
macaco1.comer("maça")
macaco1.comer("pedra")
macaco1.digerir()

macaco2 = Macaco("bobao")
macaco2.comer(macaco1)

# • Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y.
# b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
# c. Possua uma função para imprimir os valores da classe Ponto
# d. Possua uma função para encontrar o centro de um Retângulo.
# e. Você deve criar alguns objetos da classe Retangulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
# retângulo, que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
# ponto que indique os valores de x e y para o centro do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def imprimePonto(self):
        print (f"x: {self.x}, y: {self.y}")
    def centro(self):
        centro = (f"({self.x/2},{self.y/2})")
        return centro
    

class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def centro(self):
        print(f"Centro da largura: {self.largura / 2}\nCentro da altura: {self.altura / 2}")
        centro = Ponto(self.largura, self.altura)
        print("Centro do retângulo: " + centro.centro())
        opcao = input("Deseja alterar os valores do retângulo? 1 para sim, 2 para não: ")
        if opcao == "2":
            return print("Reiniciando operação...")
        elif opcao == "1":
            newValueX = input("Informe o valor de x: ")
            newValueY = input("Informe o valor de y: ")
            novoReta = Retangulo(int(newValueX), int(newValueY))
            novoReta.centro()
        else:
            return print("Opção inválida.")

novoRetangulo = Retangulo(0,0)
novoRetangulo.centro()


# • Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro
# iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
# quantidade de litros que foi colocada no veículo
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
# combustível e mostra o valor a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na
# bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
# combustível total na bomba.

class bombaCombustivel():
    def __init__(self):
        self.tipoCombustivel = ["Gasolina", "Etanol", "Diesel"]
        self.valorLitro = [5.54, 4.49, 5.99]
        self.quantidadeCombustivel = [100, 100, 100]
    
    def abastercerPorValor(self, valor, tipo):
        total = valor / self.valorLitro[tipo]
        print(f"Foram abastecidos: {valor / self.valorLitro[tipo]} litros de {self.tipoCombustivel[tipo]}")
        self.alterarQuantidadeCombustivel(total, tipo)

    def abastecerPorLitro(self, litros, tipo):
        print(f"Foram abastecidos: {litros} litros por R${litros * self.valorLitro[tipo]}")
        self.alterarQuantidadeCombustivel(litros, tipo)
    def alteraValor(self, novoValor):
        self.valorLitro = novoValor
    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel
    def alterarQuantidadeCombustivel(self, quantidade, tipo):
        self.quantidadeCombustivel[tipo] -= quantidade
        print(f"Quantidade do tanque da bomba de {self.tipoCombustivel[tipo]}: {self.quantidadeCombustivel[tipo]}")

carro = bombaCombustivel()
combustivel = input("Informe o tipo de combustivel a ser abastecido: ")
qtd = input(f"O valor do litro do {combustivel} é: valor Informe a quantidade em litros")
carro.abastercerPorValor(100, 0)