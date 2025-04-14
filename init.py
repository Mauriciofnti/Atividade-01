import time

class Init():
    def __init__(self, bola):
        self.bola = bola
        self.quadrado = Quadrado()
        self.retangulo = Retangulo(5,10)
        self.conta = False
        self.teve = Teve()
        self.tamagushi = {}
        self.macaco = {}
        self.posto = BombaCombustivel()
        
        self.opcaoPrincipal()
        
        # pass
    
    def opcaoPrincipal(self):
        while True:
            self.opcao = input("\nINITTTTTTTTTTTTTTTTTTTTTTTTTTTTT: \n"
                            "|-----------------------------------|\n"
                            "| 1 - Classe Bola.                  |\n"
                            "| 2 - Classe Quadrado.              |\n"
                            "| 3 - Classe Retangulo.             |\n"
                            "| 4 - Classe Pessoa(off).           |\n"
                            "| 5 - Classe ContaCorrente.         |\n"
                            "| 6 - Classe Teve.                  |\n"
                            "| 7 - Classe Tamagushi.             |\n"
                            "| 8 - Classe Macaco(off).           |\n"
                            "| 9 - Classe Ponto(off).            |\n"
                            "| 10 - Classe Posto de Combustível. |\n"
                            "|-----------------------------------|\n"
                            )
            match int(self.opcao):
                case 1:
                    # Bola().menuBola()
                    self.bola.menuBola()
                case 2:
                    self.quadrado.menuQuad()
                case 3:                                        
                    self.retangulo.menuRetang()     
                case 5:
                    if self.conta:
                        self.conta.menuConta()                        
                    else:                        
                        num = input("Informe o número da conta corrente: ")
                        nome = input("Informe o nome do proprietário da conta: ")                    
                        self.conta = ContaCorrente(num, nome)
                        self.conta.menuConta()                        
                case 6:
                    # from classes.teve import Teve
                    # novaTeve = Teve()
                    # novaTeve.menuTeve()
                    self.teve.menuTeve()
                    
                case 7:
                    print(f"Você possui {len(self.tamagushi)} Tamagushis: ", end="")
                    if len(self.tamagushi) == 1:
                        print(list(self.tamagushi.keys()))
                        opt = input("1 - Acessar Tama\n2 - Criar Tama\n")
                        match int(opt):
                            case 1:
                                nome = list(self.tamagushi.keys())[0]
                                print(nome)
                                self.tamagushi[nome].menuTama()
                            case 2:
                                nome = input("Informe o nome do novo Tamagushi: ")
                                self.tamagushi[nome] = Tamagushi(nome, self.tamagushi)
                                self.tamagushi[nome].menuTama() 
                    elif len(self.tamagushi) > 1:
                        print(list(self.tamagushi.keys()))
                        nome = input("Informe o nome do Tamagushi a ser acessado: ")
                        if nome in list(self.tamagushi.keys()):
                            self.tamagushi[nome].menuTama()
                        else:
                            print("Informe o nome correto...")
                            time.sleep(1)
                    else:
                        nome = input("\nInforme o nome do novo Tamagushi: ")
                        self.tamagushi[nome] = Tamagushi(nome, self.tamagushi)
                        self.tamagushi[nome].menuTama()
                case 8:
                    # print(self.macaco[0].nome)
                    print(list(self.macaco.keys()))
                    
                    if len(self.macaco) == 0:
                        nomeMacaco = input("Informe o nome do novo macaco: ")
                        self.macaco[nomeMacaco] = Macaco(nomeMacaco, self.macaco)
                        
                        self.macaco[nomeMacaco].menuMacaco()
                    elif len(self.macaco) == 1:

                        print(f"Você possui o macaco: {list(self.macaco.keys())[0]}")
                        option = input("Informe a opção:\n 1-Acessar macaco\n2-Criar macaco\n3-Deletar macaco")
                        match int(option):
                            case 1:
                                self.macaco[list(self.macaco.keys())[0]].menuMacaco()                                    
                            case 2:
                                nome = input("Informe o nome do novo macaco: ")
                                self.macaco[nome] = Macaco(nome, self.macaco)
                                self.macaco[nome].menuMacaco()
                            case 3:
                                nome = input("Informe o nome do macaco a ser deletado: ")
                                del self.macaco[nome]
                                print(self.macaco)
                                time.sleep(2)
                                self.opcaoPrincipal()
                                
                        

                    else:
                        for i in list(self.macaco.keys()):
                            print(f"Você possui o macaco: {i}")
                        mac = input(f"Informe o nome do macaco a ser escolhido: ")
                        if mac in list(self.macaco.keys()):
                            self.macaco[mac].menuMacaco()
                        else:
                            print("Nome não encontrado...")
                        
                    # self.macaco[0].menuMacaco()
                case 10:
                    self.posto.menuPosto()
                case 00:
                    from main import MenuPrincipal
                    MenuPrincipal().opcaoPrincipal()
                case _:
                    print("\n***Digite um valor válido...***\n")
                    self.opcaoPrincipal()
                
class Bola:
    cor = "Verde"
    circunferencia = 69
    material = "Plástico"  
    # volta = Init().opcaoPrincipal()  

    def trocaCor(self, novaCor): 
        self.cor = novaCor
    def mostraCor(self):
        print(f"Cor da bola: {self.cor} \n")
    def menuBola(self):
        while True:
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
                    return
                case 2:
                    self.mostraCor()  
                    self.menuBola() 
                    return             
                case 0:
                    # self.opcaoPrincipal()
                    # Init().opcaoPrincipal() 
                    return

class Quadrado:
    tamanhoLado = 0

    def mudaValorDoLado(self):
        novoValor = input("Informe o novo valor do lado em cm: ")
        self.tamanhoLado = novoValor
        print(f"\n | Lado alterado para: {novoValor} cm. |\n")
    def retornaValorDoLado(self):
        print(f"\n | O valor do lado é {self.tamanhoLado} cm. |\n")
    def calculaArea(self):
        print(f"\n | A area do quadrado é de {int(self.tamanhoLado) * 4} cm. |\n")
    def menuQuad(self):
        while True:
            option = input("Informe a opção desejada: \n |1 - Alterar valor do lado quadrado.\n |2 - Retorna valor do lado.\n |3 - Calcular area do quadrado. \n |0 - Voltar ao menu anterior.\n")
            match int(option):
                case 1:
                    self.mudaValorDoLado()
                    self.menuQuad()
                    return
                case 2:
                    self.retornaValorDoLado()
                    self.menuQuad()
                    return
                case 3:
                    self.calculaArea()
                    self.menuQuad()
                    return
                case 0:
                    return
                
class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.area = int(self.ladoA) * int(self.ladoB)
        self.perimetro = (int(self.ladoA) * 2) + (int(self.ladoB) * 2)

    def mudaValorLado(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB
        self.retornaValorLados()
        
    def retornaValorLados(self):
        print(f"\nO valor dos lados é: \nBase: {self.ladoA}m, \nAltura: {self.ladoB}m.\n")
        
    def calculaArea(self):
        self.area = int(self.ladoA) * int(self.ladoB)
        print(f"\nO valor da área desse retangulo é {self.area}m².\n")
        
    def calculaPeri(self):
        self.perimetro = (int(self.ladoA) * 2) + (int(self.ladoB) * 2)
        print(f"\nO perimetro do retangulo é {(int(self.ladoA) + int(self.ladoB)) * 2}m.\n")
        
    def calcularPisos(self):
        self.calculaArea()
        self.calculaPeri()
        pisos = self.area / 0.25
        rodapes = self.perimetro / 0.15
        print(
                f"\nConsiderando pisos de 50x50 cm serão necessários no minimo {int(pisos)} pisos para preencher uma área de {self.area} m²,"
                f"e {rodapes:.2f} rodapés de 15 cm cada.\n"
              )
    
    def menuRetang(self):
        while True:
            # altura = self.ladoA
            # largura = self.ladoB
            # altura2 = self.ladoA
            # largura2 = self.ladoB
            # for i in range(altura):
            #     if i == 0 or i == altura - 1:
            #         print("_" * largura)
            #     else:
            #         print("|" + " " * (largura - 2) + "|")
            option = input(
                f"LADOS: {self.ladoA}, {self.ladoB}\n"
                "|** Informe a opção desejada:                  |\n"
                "| 1 - Alterar valor do lado retangulo.         |\n"
                "| 2 - Retorna valor do lado.                   |\n"
                "| 3 - Calcular área do retangulo.              |\n"
                "| 4 - Calcular perimetro do retangulo.         |\n"
                "| 5 - Calcular quantidade de pisos e rodapés.  |\n"
                "| 0 - Voltar ao menu anterior.                 |\n"
                )

            match int(option):
                case 1:
                    ladoA = int(input("Informe o novo valor da base do retangulo em metros: "))
                    ladoB = int(input("Informe a novo valor da altura do retangulo em metros: "))
                    self.mudaValorLado(ladoA, ladoB)
                    self.menuRetang()
                    return
                case 2:
                    self.retornaValorLados()
                    self.menuRetang()
                    return
                case 3:
                    self.calculaArea()
                    self.menuRetang()
                    return
                case 4:
                    self.calculaPeri()
                    self.menuRetang()
                    return
                case 5:
                    self.calcularPisos()
                    self.menuRetang()
                    return
                case 0:
                    return 
  
class ContaCorrente():
    def __init__(self, numConta, nome, saldo=0):
        self.numConta = numConta
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    
    def deposito(self, valor):
        self.saldo += int(valor)
        return self.saldo
    
    def saque(self, valor):
        self.saldo -= int(valor)
        return self.saldo
    
    def menuConta(self):
        option = input(
                f"|** Olá Senhor {self.nome}...  SALDO R${self.saldo}\n"
                f"|\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Alterar Nome.               |\n"
                 "| 2 - Depositar.                  |\n"
                 "| 3 - Sacar.                      |\n"
                 "| 0 - Sair.                       |\n"
                )
        while True:
            match int(option):
                case 1:
                    novoNome = input("Informe o novo nome: ")
                    self.alterarNome(novoNome)
                    self.menuConta()
                    return
                case 2:
                    valor = input("Informe o valor a ser depositado: ")
                    self.deposito(valor)
                    print(f"O deposito no valor de R${valor} foi efetuado com sucesso, seu novo saldo é de R${self.saldo}.\n")
                    self.menuConta()
                    return
                case 3:
                    valor = input("Informe o valor a ser sacado: ")
                    if float(valor) > self.saldo:
                        print("Seu saldo não é suficiente..")
                        self.menuConta()
                        return
                    else:
                        self.saque(valor)
                        print(f"O saque no valor de R${valor} foi efetuado com sucesso, seu novo saldo é de R${self.saldo}.\n")
                        self.menuConta()
                        return
                case 0:
                    return              
 
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
                 f"\nSintonizado no canal: {self.canais[self.canal]}\nVolume: {self.volume}\n"
                 "|** Informe a opção desejada:     |\n"
                 "| 1 - Trocar Canal.               |\n"
                 "| 2 - Mudar Volume.               |\n"
                 "| 0 - Sair.                       |\n"
                )
        while True:
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
                    return
                case 2:
                    volume = input("Informe o valor do volume (0-100): ")
                    self.mudarVolume(volume)
                    self.menuTeve()
                    return

                case 0:
                    return             

class Tamagushi():
    def __init__(self, nome, agrupamento):
        self.nome = nome
        self.agrupamento = agrupamento
        self.fome = 10
        self.saude = 10
        self.idade = 0
    
    def deletar(self):
        if self.nome in self.agrupamento:
            del self.agrupamento[self.nome]
            print("Game Over!!!\n" * 5)
            print(f"Tamagushi '{self.nome}' foi deletado.")
            time.sleep(2)
        else:
            print(f"Tamagushi '{self.nome}' não encontrado.")
            time.sleep(2)

    def alterarNome(self, newName):
        old_name = self.nome
        self.nome = newName
        self.agrupamento[newName] = self.agrupamento.pop(old_name)
        print(f"Nome alterado para '{newName}'.")
        time.sleep(2)
        
    def alteraFome(self):
        fome = input("Informe a fome entre valores:\n0 - MUITA fome\n10 - SEM fome\n")
        try:
            self.fome = int(fome)
        except:
            print("Informe uma opção entre 0 e 10 (somente números).")
            return
        if int(fome) == 0:
            print(f"Você matou o {self.nome} :O")
            time.sleep(3)
            print(";'(")
            self.deletar()
            return
        else:
            self.menuTama()
            
    def alteraSaude(self):
        saude = input("Informe a saúde entre valores:\n0 - MUITA saúde\n10 - SEM saúde\n")
        self.saude = int(saude)
        if self.saude <= 0:
            self.deletar()
            return
        else:
            self.menuTama()
    
    def alteraIdade(self):
        idade = input(f"Informe a idade de {self.nome}: ")
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
                 "| 5 - Deletar Tamagushi.          |\n"
                 "| 0 - Sair.                       |\n"
                )
        while True:
            match int(option):
                case 1:
                    novoNome = input("Informe o novo nome: ")
                    self.alterarNome(novoNome)
                    self.menuTama()
                    return
                case 2:
                    self.alteraFome()
                    return                    
                case 3:
                    self.alteraSaude()
                    return
                case 4:
                    self.alteraidade()
                    self.menuTama()
                    return
                case 5:
                    self.deletar()
                    return
                case 0:
                    return
                case _:
                    print("\n***Digite uma opção válida...***\n")
                    time.sleep(1)   
                    self.menuTama()
                    return

class Macaco():
    def __init__(self, nome, ref):
        self.nome = nome
        self.ref = ref
        self.bucho = []

    def deletarMacaco(self):
        if self.nome in list(self.ref):
            del self.ref[self.nome]        
    
    def comer(self, comida):
        self.bucho.append(comida)
        return print(self.verBucho())
    
    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho.pop()
    
    def menuMacaco(self):
        while True:
            print(f"Você possui um macaco de nome {self.nome}.")
                  
            option = input(
                            "|** Informe a opção desejada:  |\n"
                            "| 1 - Comer.                   |\n"
                            "| 2 - Ver Bucho.               |\n"
                            "| 3 - Digerir.                 |\n"
                            "| 4 - Deletar.                 |\n"
                            "| 0 - Voltar ao menu anterior. |\n"
            )
            match int(option):
                case 1:
                    comida = input("Informe a comida: \n1-Maçã\n2-Banana\n3")
                    self.comer("")
                    
                case 2:
                    self.verBucho()
                    return             
                case 3:
                    self.digerir()
                case 4:
                    self.deletarMacaco()
                    return
                case 0:
                    return                    

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
            case 5:
                self.alterarQuantidadeCombustivel()
                self.menuPosto()
            case 0:
                return
            case _:
                print("\n***Digite um valor válido...***\n")
                self.menuPosto()


if __name__ == "__main__":
    Init(Bola())
    