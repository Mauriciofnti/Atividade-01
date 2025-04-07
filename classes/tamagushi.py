# • Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
# este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então
# não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a
# qualquer momento.
import time

class Tamagushi():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 10
        self.saude = 10
        self.idade = 0

    def alterarNome(self, newName):
        self.nome = newName
        
    def alteraFome(self, fome):
        if fome == 0:
            print("Game Over!!!\n" * 50)
        else:           
            self.fome = int(fome)
            
    def alteraSaude(self):
        saude = input("Informe a saúde entre valores:\n0 - MUITA saúde\n10 - SEM saúde\n")
        self.saude = int(saude)
    
    def alteraIdade(self):
        idade = input(f"Indorme a idade de {self.nome}: ")
        self.idade = int(idade)
            
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
            return ("Infeliz :S")
        elif self.fome <= 6 or self.saude <= 6:
            return ("Sem humor :|")
        elif self.fome <= 8 or self.saude <= 8:
            return ("Feliz :)")
        else:
            return ("Muito feliz :D")
        
    def menuTama(self):
        option = input(
                f"\n|**Nome: {self.retornaNome()}...\n"
                f"|  FOME: {self.retornaFome()}\n|  HUMOR: {self.humor()}\n|  SAUDE: {self.retornaSaude()}\n|  IDADE: {self.retornaIdade()}\n"
                f"|\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Alterar Nome.               |\n"
                 "| 2 - Alterar Fome.               |\n"
                 "| 3 - Alterar Saúde.              |\n"
                 "| 4 - Alterar Idade.              |\n"
                 "| 0 - Sair.                       |\n"
                )
        match int(option):
            case 1:
                novoNome = input("Informe o novo nome: ")
                self.alterarNome(novoNome)
                self.menuTama()
            case 2:
                fome = input("Informe a fome entre valores:\n0 - MUITA fome\n10 - SEM fome\n")

                if int(fome) == 0:
                    print(f"Você matou o {self.nome} :O")
                    time.sleep(3)
                    print(";'(")
                    time.sleep(2)
                    self.alteraFome(int(fome))
                    time.sleep(1)
                    self.volta()
                self.menuTama()
            case 3:
                self.alteraSaude()
                self.menuTama()
            case 4:
                self.alteraidade()
                self.menuTama()
            case 0:
                self.volta()
    def volta(self):
        from main import MenuPrincipal
        volta = MenuPrincipal()
        volta.opcaoPrincipal()