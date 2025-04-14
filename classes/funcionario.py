# • Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e
# um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para
# devolver nome e salário. Escreva um pequeno programa que teste sua classe.
# • Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
# (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# • Exemplo de uso:
# harry = funcionário("Harry",25000)
# harry.aumentarSalario(10)
import time

class Funcionario():
    def __init__(self, nome):
        self.nome = nome
        salario = input(f"Informe o salário de {self.nome}: R$")
        self.__salario = float(salario)
    
    def devolverNome(self):
        print(f"Nome: {self.nome}")
    
    def devolveSalario(self):
        print(f"Salário: {self.__salario}.")

    def percentualDeAumento(self):
        perc = input(f"Informe o percentual a ser aumentado no salário de {self.nome}: ")
        self.__salario += self.__salario * (float(perc)/100)
        print(f"Novo salário de {self.nome}: R${self.__salario}")
    
    def menuFuncionario(self):
        option = input(
                f"|** FUncionário: {self.nome}...\n"
                f"|\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Ver nome.                   |\n"
                 "| 2 - Ver salário.                |\n"
                 "| 3 - Aumentar salário por %.     |\n"
                 "| 0 - Sair.                       |\n"
                )
        match int(option):
            case 1:
                self.devolverNome()
                time.sleep(2)
                self.menuFuncionario()
            case 2:
                self.devolveSalario()
                time.sleep(2)
                self.menuFuncionario()
            case 3:
                self.percentualDeAumento()
                time.sleep(2)
                self.menuFuncionario()
            case 0:
                from main import MenuPrincipal
                volta = MenuPrincipal()
                volta.opcaoPrincipal()
