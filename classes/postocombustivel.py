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
import time

class BombaCombustivel():
    def __init__(self):
        self.tipoCombustivel = ["1-Gasoli", "2-Etanol", "3-Diesel"]
        self.combListName = {"1":"gasolina", "2":"etanol", "3":"diesel"}
        self.valorLitro = [5.54, 4.49, 5.99]
        self.quantidadeCombustivel = [1000, 1000, 1000]
        self.tanque = dict(zip(self.tipoCombustivel, self.quantidadeCombustivel))
        self.precos = dict(zip(self.tipoCombustivel, self.valorLitro))
        self.nome_exibicao = dict(zip(self.combListName.values(), self.tipoCombustivel))
    
    def abastercerPorValor(self):     
        self.banner()
        tipo = self.procuraComb("abastecido")   
        # comb = input("Informe o nome ou número do combustivel a ser abastecido: \n").strip().lower()

        # if comb not in self.combListName and comb.lower() not in self.combListName.values():
        #     print("Informe o combustivel correto.")
        #     return
        # else:
        #     tipo = "Agua"
        #     if comb in self.combListName.keys():
        #         tipo = self.nome_exibicao[self.combListName[comb]]
        #     elif comb in self.combListName.values():
        #         tipo = self.nome_exibicao[comb]
        #     else:
        #         print("error")
                
        #     # print(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}")
        valor = input(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}\nInforme o valor de combustivel a ser abastecido em R$:")
        total = int(valor) / self.precos[tipo]
        
        print(f"Foram abastecidos: {total:.3f} litros de {tipo}")
        self.atualizaTanque(tipo, total)
        time.sleep(2)

    def abastecerPorLitro(self):
        self.banner()
        tipo = self.procuraComb("abastecido")
        # comb = input("Informe o nome ou número do combustivel ser abastecido: ")          
        litros = input(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}\nInforme a quantidade de litros a ser abastecida:")

        total = int(litros) * self.precos[tipo]
        print(f"Foram abastecidos {litros} litros de {tipo} pelo valor de R${total:.2f}.")
        time.sleep(2)
        self.atualizaTanque(tipo, float(litros))
    
    def atualizaTanque(self, comb, litros):
        self.tanque[comb] -= litros
        
    def procuraComb(self, text):
        comb = input(f"Informe o nome ou número do combustivel a ser {text}: \n").strip().lower()

        if comb not in self.combListName and comb.lower() not in self.combListName.values():
            print("Informe o combustivel correto.")
            time.sleep(2)
            return
        else:
            tipoDeComb = "Agua"
            if comb in self.combListName.keys():
                tipoDeComb = self.nome_exibicao[self.combListName[comb]]
            elif comb in self.combListName.values():
                tipoDeComb = self.nome_exibicao[comb]
            else:
                print("error")
            return tipoDeComb
            # print(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}")
            # valor = input(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}\nInforme o valor de combustivel a ser abastecido em R$:")
            # total = int(valor) / self.precos[tipo]
            
            # print(f"Foram abastecidos: {total:.3f} litros de {tipo}")
            # self.atualizaTanque(tipo, total)
            # time.sleep(2)
        
    def alteraValor(self):
        self.banner()
        tipo = self.procuraComb("alterado")
        if tipo:            
            novoValor = input(f"Informe o novo valor de {tipo}: ")
            self.precos[tipo] = int(novoValor)
            print(f"Valor de {tipo} foi alterado para R${novoValor} por litro")        
        else:
            return
        
        time.sleep(2)

        # print(str(self.precos))
        # print(tipo)
        # print("Valor alteradooo")
        
        
    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel
        
    def alterarQuantidadeCombustivel(self, quantidade, tipo):
        self.tanque[tipo] -= quantidade
        print(f"Quantidade do tanque da bomba de {tipo}: {self.tanque[tipo]}")

    def banner(self):
        print("\n************POSTO DO DOUTOR PC************\n\nCombustivel:                 Tanque:")
        print(*[
                    f"{comb}: R$ {self.precos[comb]:.2f} |            {self.tanque[comb]:.2f} litros"
                    for comb in self.tipoCombustivel
                ], sep="\n"
              )
        print("")

    def menuPosto(self):
        self.banner()
        
        option = input(
                 "|** Informe a opção desejada:             |\n"
                 "| 1 - Abastecer por valor $.              |\n"
                 "| 2 - Abastecer por litros.               |\n"
                 "| 3 - Alterar valor.                      |\n"
                 "| 4 - Alterar combustivel.                |\n"
                 "| 5 - Alterar quantidade de combustivel.  |\n"
                 "| 0 - Sair.                               |\n"
                )
        match int(option):
            case 1:
                self.abastercerPorValor()
                self.menuPosto()                
            case 2:
                self.abastecerPorLitro()
                self.menuPosto()
            case 3:
                self.alteraValor()
                self.menuPosto()
            case 4:
                self.alteraidade()
                self.menuTama()
            case 0:
                self.volta()
    
carro = BombaCombustivel()
carro.menuPosto()