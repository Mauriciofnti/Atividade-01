
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
        # return print(self.verBucho())

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho.pop()

macaco1 = Macaco("bob")
macaco1.comer("banana")
macaco1.comer("maça")
macaco1.comer("pedra")
# macaco1.digerir()


macaco2 = Macaco("bobao")
macaco2.comer(macaco1)
macaco2.digerir()
print(macaco2.bucho)


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
    
    def menuMacaco(self):
        while True:
            print(f"Você possui um macaco de nome {self.nome}."
                  f"Bucho : {self.verBucho()}")
                  
            option = input(
                            "|** Informe a opção desejada: |\n"
                            "| 1 - Mudar a cor da bola.    |\n"
                            "| 2 - Mostrar a cor da bola.  |\n"
                            "| 0 - Voltar ao menu anterior.|\n"
            )
            match int(option):
                case 1:
                    novaCor =  input("Informe a nova cor da bola:")
                    self.trocaCor(novaCor)
                    self.mostraCor()
                    self.menuBola()
                    return
                case 2:
                    self.mostraCor()  
                    self.menuBola() 
                    return             
                case 0:
                    # self.opcaoPrincipal()
                    # Init().opcaoPrincipal() 
                    return