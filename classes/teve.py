# • Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
# ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o
# número do canal e o nível do volume permanecem dentro de faixas válidas.

class Teve():
    def __init__(self):
        self.canais =  {0: "Desligado", 5: "Algum canal", 10: "Outro canal" , 50: "Um canal qualquer", 60: "Ultimo canal"}
        self.canal = 0
        self.volume = 0   

    def mudarCanal(self, novoCanal):
        
        if novoCanal not in self.canais:
            print("Canal inválido")
            self.menuTeve()
        else:
            self.canal = novoCanal
            return (f"Sintonizado no canal: {self.canais[novoCanal]}")
    def mudarVolume(self, novoVolume):
        if int(novoVolume) <= 0 or int(novoVolume) > 100:
            print("Volume inválido")
        else:
            self.volume = novoVolume
            return (f"O volume está em: {self.volume}")
    def menuTeve(self):
        option = input(
                 f"\nSintonizado no canal {self.canais[self.canal]}\nVolume: {self.volume}\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Trocar Canal.               |\n"
                 "| 2 - Mudar Volume.               |\n"
                 "| 0 - Sair.                       |\n"
                )
        match int(option):
            case 1:
                novoCanal = input(
                        "Informe o canal desejado:\n"
                        "05 - Algum canal\n"
                        "10 - Outro canal\n"
                        "50 - Um canal qualquer\n"
                        "60 - Ultimo canal\n"                        
                    )
                self.mudarCanal(int(novoCanal))
                self.menuTeve()
            case 2:
                volume = input("Informe o valor do volume (0-100): ")
                self.mudarVolume(volume)
                self.menuTeve()

            case 0:
                from main import MenuPrincipal
                volta = MenuPrincipal()
                volta.opcaoPrincipal()
