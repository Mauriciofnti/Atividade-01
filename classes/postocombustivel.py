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
        valor = input(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}\nInforme o valor de combustivel a ser abastecido em R$:")        
        total = int(valor) / self.precos[tipo]
        if self.confereTanque(tipo, total):        
            print(f"Foram abastecidos: {total:.3f} litros de {tipo}")
            self.atualizaTanque(tipo, total)
            time.sleep(2)
        else:
            return
    
    def abastecerPorLitro(self):
        self.banner()
        tipo = self.procuraComb("abastecido")        
        litros = input(f"Tipo: {tipo} \nPreço por litro: {self.precos[tipo]}\nInforme a quantidade de litros a ser abastecida:")
        total = int(litros) * self.precos[tipo]
        if self.confereTanque(tipo, litros):
            print(f"Foram abastecidos {litros} litros de {tipo} pelo valor de R${total:.2f}.")
            time.sleep(2)
            self.atualizaTanque(tipo, float(litros))
        else:
            return
    
    def confereTanque(self, tipo, qtd):
        if int(qtd) > self.tanque[tipo]:
            print(f"\nQuantidade no tanque insuficiente. Quantidade atual: {self.tanque[tipo]}.")
            time.sleep(2)
            return False
        else:
            return True
    

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
        
        
    def alterarCombustivel(self):
        self.banner()
        combustivel = self.procuraComb("alterado")
        if combustivel:
            novaQtd = input(f"Informe a nova quantidade do tanque de {combustivel}")
            self.tanque[combustivel] = int(novaQtd)
        else:
            return
        
        
    def alterarQuantidadeCombustivel(self):
        self.banner()
        combustivel = self.procuraComb("alterado")
        if combustivel:
            novaQtd = input(f"Informe a nova quantidade do tanque de {combustivel}: ")
            self.tanque[combustivel] = float(novaQtd)
            print(f"Quantidade do tanque da bomba de {combustivel} alterado para: {self.tanque[combustivel]} litros.")
        else:
            return
        time.sleep(2)     

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
                 "| 4 - Alterar combustivel.(off)           |\n"
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
            # case 4:
            #     self.alteraidade()
            #     self.menuTama()
            case 5:
                self.alterarQuantidadeCombustivel()
                self.menuPosto()
            case 0:
                self.volta()
            case _:
                print("\n***Digite um valor válido...***\n")
                self.opcaoPrincipal()
    
    def volta(self):
        from main import MenuPrincipal
        volta = MenuPrincipal()
        volta.opcaoPrincipal()