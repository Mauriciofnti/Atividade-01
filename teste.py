# • Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago)
# e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
# criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
# verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o
# outro. É possível criar um macaco canibal?

class Macaco():
    def __init__(self, nome):
        self.__nome = nome
        self.bucho = []
    
    def comer(self, comida):
        self.bucho.append(comida)
        return self.verBucho()
    
    def verBucho(self):
        print(f"Você possuí isso de bomida no bucho do {self.__nome}: ")
        if len(self.bucho) == 0:
            print(f"O {self.__nome} está de bucho vazio!!!")
        else:            
            for coco in self.bucho:
                if type(coco) == type(self):
                    print(f"Você comeu o {coco.__nome} ????? ")
                else:
                    print(f"{coco} ")
            # return self.bucho

    def digerir(self):
        self.bucho.pop()
    
    def alteraNome(self, newName):
        self.__nome = newName

macaco1 = Macaco("bob")
macaco1.comer("banana")
macaco1.comer("maça")
macaco1.comer("pedra")
macaco1.digerir()
macaco1.verBucho()

macaco2 = Macaco("bobao")
macaco2.comer(macaco1)
macaco2.digerir()
macaco2.verBucho()
# novoNome = input("Informe o novo nome do Macaco: ")
# macaco1.alteraNome(novoNome)
# print(novoNome)