# • Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário
# especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
# Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

from tamagushi import Tamagushi

class BichinhoMaisMais(Tamagushi):
    def __init__(self, nome):
        super().__init__(nome)
        self.qtdComida = 10
        self.qtdBrinca = 10
        
bichi = BichinhoMaisMais(("bic"))
bichi.menuTama()