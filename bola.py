# • Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor



class Bola():
    cor = "Verde"
    circunferencia = 69
    material = "Plástico"    

    def trocaCor(self, novaCor): 
        self.cor = novaCor
    def mostraCor(self):
        print(f"Cor da bola: {self.cor} \n")
    def menuBola(self):
        print(f"Você possui uma bola de cor {self.cor}, com circunfêrencia de {self.circunferencia} cm e de um material {self.material}.")
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
            case 2:
                self.mostraCor()  
                self.menuBola()              
            case 0:
                from main import MenuPrincipal
                volta = MenuPrincipal()
                volta.opcaoPrincipal()       

