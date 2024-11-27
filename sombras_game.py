#Primeiro, importamos o módulo random, que nos permite gerar números aleatórios
import random

#Dictionary to define the stats of the classes
guerreiro = {"vida": 60, "ataque_min": 7, "ataque_max": 14, "acerto_min": 6, "defesa_max": 12}
mago = {"vida": 40, "ataque_min": 9, "ataque_max": 18, "acerto_min": 7, "defesa_max": 15}
ladino = {"vida": 30, "ataque_min": 8, "ataque_max": 20, "acerto_min": 7, "defesa_max": 15}
itens = ["anel de força", "poção de cura"]

#Colocamos todos os dicionarios de classes como uma sublista na lista de classes
classes = [guerreiro, mago, ladino]

#Variáveis ​vazias ​de vida e stats (estatísticas) de ambos os jogadores
vida_jogador1 = 0
vida_jogador2 = 0
pocao_usada_jogador1 = False
pocao_usada_jogador2 = False

#Função para uma arte ascii do logotipo
def display_logo():
    logo = """

        ___________                           __                      .___                 _________             ___.                        
        \_   _____/ ____   ____  ____   _____/  |________  ____     __| _/____    ______  /   _____/ ____   _____\_ |______________    ______
        |    __)_ /    \_/ ___\/  _ \ /    \   __\_  __ \/  _ \   / __ |\__  \  /  ___/  \_____  \ /  _ \ /     \| __ \_  __ \__  \  /  ___/
        |        \   |  \  \__(  <_> )   |  \  |  |  | \(  <_> ) / /_/ | / __ \_\___ \   /        (  <_> )  Y Y  \ \_\ \  | \// __ \_\___ \ 
        /_______  /___|  /\___  >____/|___|  /__|  |__|   \____/  \____ |(____  /____  > /_______  /\____/|__|_|  /___  /__|  (____  /____  >
                \/     \/     \/           \/                          \/     \/     \/          \/             \/    \/           \/     \/ 

    """
    print(logo)

#Função para imprimir texto em negrito
def bold(text):
    return f"\033[1m{text}\033[0m"

#Função para imprimir texto vermelho
def red(text):
    return f"\033[31m{text}\033[0m"

#Função para imprimir texto verde
def green(text):
    return f"\033[32m{text}\033[0m"

#Função que permite que ambos os jogadores escolham sua classe
def escolher_classe(jogador):
    #Com "global" fazemos com que as variáveis ​​possam ser usadas, e os nomes
    global classes, stats_jogador1, stats_jogador2, nome_jogador_1, nome_jogador_2

    print("")

    #Mensagem de boas-vindas, que também informa as turmas
    print("‧₊˚✧ Bem-vindo ao jogo: 'Encontro das Sombras'! Guerreiros, Magos e Ladinos esperam por você. ✧˚₊‧")

    #Determina o nome do jogador com base no parâmetro "jogador"
    if jogador == "Jogador 1":
        nome_jogador_1 = input(f"Jogador 1, {bold('qual é o nome do herói?')} Sua jornada nas sombras começa agora: ")
        nome_jogador = nome_jogador_1

    else:
        nome_jogador_2 = input(f"Jogador 2, {bold('qual é o nome do herói?')} Sua jornada nas sombras começa agora: ")
        nome_jogador = nome_jogador_2

    #Nome do jogador que escolhe a classe
    print(f"{nome_jogador}, sua jornada nas sombras começa agora! \n")

    #Aventura começa! Primeiro, escolha sua classe: 1 para ser Guerreiro, 2 para Mago ou 3 para Ladino.
    print("Primeiro, escolha sua classe: 1 para Guerreiro, 2 para Mago ou 3 para Ladino.")

    #Inicio de um loop "while", o programa continua perguntando até que o jogador escolha um número de classe válido\
    while True:
        # Variável de escolha criada, para que o jogador escolha sua classe
        if jogador == "Jogador 1":
            escolha = int(input(f"{nome_jogador_1}, {bold('escolha sua classe')}!: "))
        else:
            escolha = int(input(f"{nome_jogador_2}, {bold('escolha sua classe')}: "))

        if escolha in [1, 2, 3]:
            # Com "if" atribuímos a classe correta (com o índice - 1, então cabe 0, 1, 2), com o jogador determinado
            if jogador == "Jogador 1":
                stats_jogador1 = classes[escolha - 1]
            else:
                stats_jogador2 = classes[escolha - 1]

            if escolha ==  1:
                print(f"{jogador} escolheu ser um {bold('Guerreiro')}!( ◡̀_◡́)ᕤ Força e honra guiam seus passos, pronto para esmagar qualquer inimigo.")
            
            elif escolha == 2:
                print(f"{jogador} escolheu ser um {bold('Mago')}! (∩'-')⊃━☆ﾟ.*･｡ﾟ! O poder das artes arcanas corre em suas veias, moldando o mundo ao seu redor.")
            
            elif escolha == 3:
                print(f"{jogador} escolheu ser um {bold('Ladino')}! ᗜԅ(⇀︿⇀)ᓄ-¤]═─── Nas sombras você é invisível, ágil como uma serpente e mortal como uma lâmina.")

            # Para sair do loop se as classes escolhidas estiverem corretas
            break
        
        # Se a entrada for inválida, permite que a classe seja solicitada novamente
        else:
            print("Número inválido, escolha uma classe entre 1, 2 ou 3.")
    
    print("")
    print("✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   .  ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦")
            

#Função para definir o sistema de batalha do jogo
def batalha(vida_jogador1, stats_jogador1, vida_jogador2, stats_jogador2):
    #Criamos uma variável auxiliar para controlar a quantidade de turnos do jogo
    print("")
    turno = 0

    pocao_usada_jogador1 = False
    pocao_usada_jogador2 = False
    
    #Define os estados de defesa iniciais
    defesa_jogador1 = False
    defesa_jogador2 = False

    #Definir a vida dos jogadores, segundo o valor nas listas
    vida_jogador1 = stats_jogador1["vida"]
    vida_jogador2 = stats_jogador2["vida"]

    #Loop "While" mantém o jogo em loop e os turnos em andamento até que uma das vidas do jogador chegue a 0
    while vida_jogador1 > 0 and vida_jogador2 > 0:
        turno += 1

        #Informar o turno do jogo e a vida de ambos os jogadores
        print(f"  ───  {bold('TURNO')} {bold(str(turno))}.  ───  ")
        print(f"{nome_jogador_1} está com {vida_jogador1} de vida.")
        print(f"{nome_jogador_2} está com {vida_jogador2} de vida.")
        print("")

        print("✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   .  ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦")
        #Loop dos turnos dos jogadores
        for jogador in range(1,3):
            if jogador == 1:
                escolha = int(input(f"""
{nome_jogador_1}, {bold('escolha uma ação')}:

1 - Atacar
2 - Defender
3 - Usar um item

Digite o número correspondente à sua escolha: """))


                stats = stats_jogador1

            else:
                escolha = int(input(f"""
{nome_jogador_2}, {bold('escolha uma ação')}:

1 - Atacar
2 - Defender
3 - Usar um item

Digite o número correspondente à sua escolha: """))

                stats = stats_jogador2

            #Se a escolha for defesa
            if escolha == 2:
                #Dado de 20 lados, onde, com a ajuda de "randomint", nos dá um número inteiro aleatório
                dado = random.randint(1, 20)
                print(f"A rolagem do dado resultou em: {dado}.")
                
                #A chance de defesa depende da defesa maxima do jogador
                if dado >= stats["defesa_max"]:
                    if jogador == 1:
                        defesa_jogador1 = True
                        print(f"{nome_jogador_1} {green('está defendendo')}! Só receberá metade do dano.")
                        print("")

                    else:
                        defesa_jogador2 = True
                        print(f"{nome_jogador_2} {green('está defendendo')}! Só receberá metade do dano.")
                        print("")
                else:
                    if jogador == 1:
                        defesa_jogador1 = False
                        print(f"{nome_jogador_1} {red('falhou')} na defesa!")
                        print("")
                    else:
                        defesa_jogador2 = False
                        print(f"{nome_jogador_2} {red('falhou')} na defesa!")
                        print("")
            
            #Se a escolha for ataque
            elif escolha == 1:
                #Dado de 20 lados, de novo
                if jogador == 1:
                    print(f"{nome_jogador_1} decidiu {bold('atacar')}.")
                else:
                    print(f"{nome_jogador_2} decidiu {bold('atacar')}.")

                print("")

                dado = random.randint(1, 20)
                print(f"A rolagem do dado resultou em: {bold(dado)}.")

                #Com o índice “3” acessamos o acerto minimo com o "1" acessamos o dano minimo, e com o "2" acessamos o dano maximo
                if  dado >= stats["acerto_min"]:
                    #Se o dado estiver acima do mínimo, mas não 20, então o dano é a média do dano máximo e mínimo do jogador
                    dano = (stats["ataque_min"] + stats["ataque_max"]) // 2

                    #Se o dado for 20, sendo um acerto crítico, então é o dano máximo
                    if dado == 20:
                        dano = stats["ataque_max"]

                    #Se algum dos jogadores se defender, o dano que toma se tem que dividir
                    if jogador == 1 and defesa_jogador2:
                        dano = dano // 2
                        print(f"A defesa {green('reduz o dano')} tomado por {nome_jogador_2} pela metade!")
                    
                    elif jogador == 2 and defesa_jogador1:
                        dano = dano // 2
                        print(f"A defesa {green('reduz o dano')} tomado por {nome_jogador_1} pela metade!")

                    if jogador == 1:
                        vida_jogador2 -= dano
                        print(f"{nome_jogador_2} recebeu {red(dano)} de dano e está com {bold(vida_jogador2)} de vida!")
                        print("")

                    else:
                        vida_jogador1 -= dano
                        print(f"{nome_jogador_1} recebeu {red(dano)} de dano e está com {bold(vida_jogador1)} de vida!")
                        print("")
                
                #Se o dado estiver abaixo do mínimo, o acerto é um erro e o dano é 0
                else:
                    if jogador == 1:
                        print(f"{red('Ataque errou!')} A vida do {nome_jogador_2} não é afetada.")
                        print("")
                    
                    else:
                        print(f"{red('Ataque errou!')} A vida do {nome_jogador_1} não é afetada.")
                        print("")

            #Se a escolha for um item
            elif escolha == 3:
                if jogador == 1:
                    nome_jogador = nome_jogador_1
                else:
                    nome_jogador = nome_jogador_2
                
                escolha_item = int(input(f"{nome_jogador}, digite 1 para usar a poção ou qualquer outra tecla para cancelar: "))
                print("")

                if escolha_item == 1:
                    if jogador == 1:
                        if not pocao_usada_jogador1:
                            vida_jogador1 += 10
                            pocao_usada_jogador1 = True
                            print(f"{nome_jogador_1} foi {green('curado')}, sua vida atual agora é: {vida_jogador1} \n")

                        else:
                            print(f"{nome_jogador_1} {red('já usou')} a poção! \n")

                
                    elif jogador == 2:
                        if not pocao_usada_jogador2:
                            vida_jogador2 += 10
                            pocao_usada_jogador2 = True
                            print(f"{nome_jogador_2} foi {green('curado')}, sua vida atual agora é: {vida_jogador2} \n")
                        
                        else:
                            print(f"{nome_jogador_2} {red('já usou')} a poção! \n")
            
                else:
                    continue
    
    #Condição para encerrar o jogo, informar o vencedor, se a vida de alguém for menor ou igual a 0
    if vida_jogador1 <= 0:
        print("✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   .  ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦")
        print("")
        print(f"                                         {bold(f'{nome_jogador_2} venceu!')}")
        print("")
        print(f"Obrigado por jogar {bold('Encontro das Sombras')}! ✧˖ ⋆ Esperamos que tenha se divertido!")
        print("")
        print("✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   .  ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦")
        print("")

    elif vida_jogador2 <= 0:
        print("✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   .  ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦")
        print("")
        print(f"                                         {bold(f'{nome_jogador_1} venceu!')}")
        print("")
        print(f"Obrigado por jogar {bold('Encontro das Sombras')}! ✧˖ ⋆ Esperamos que tenha se divertido!")
        print("")
        print("✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   .  ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦  .  ⁺   . ✦ .  ⁺   . ✦")
        print("")

#Função do jogo final
def jogo():
    display_logo()
    escolher_classe("Jogador 1")
    escolher_classe("Jogador 2")
    batalha(vida_jogador1, stats_jogador1, vida_jogador2, stats_jogador2)

#Usando a função para iniciar o jogo
jogo()          