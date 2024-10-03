#Primeiro, importamos o módulo random, que nos permite gerar números aleatórios
import random

#Listas para definir a vida, ataque minimo, ataque máximo, acerto minimo e defesa máxima do guerreiro, do mago e do ladino
guerreiro = [60, 7, 14, 6, 12]
mago = [40, 9, 18, 7, 15]
ladino = [30, 8, 20, 7, 15]
itens = ["poção de cura"]

#Colocamos todas as classes como uma sublista na lista de classes
classes = [guerreiro, mago, ladino]

#Variáveis vazias de vida e stats (estatísticas) de ambos os jogadores
vida_jogador1 = 0
vida_jogador2 = 0
stats_jogador1 = []
stats_jogador2 = []



#Função que permite que ambos os jogadores escolham sua classe
def escolher_classe(jogador):
    #Mensagem de boas-vindas, que também informa as turmas
    print("Bem-vindo ao jogo: 'Encontro das Sombras'! Guerreiros, Magos e Ladinos esperam por você.")
    print("A aventura começa! Primeiro, escolha sua classe: 1 para ser Guerreiro, 2 para Mago ou 3 para Ladino.")

    #Com "global" fazemos com que as variáveis possam ser usadas
    global classes, stats_jogador1, stats_jogador2

    #Inicio de um loop "while", o programa continua perguntando até que o jogador escolha um número de classe válido\
    while True:
        #Variável de escolha criada, para que o jogador escolha sua classe
        escolha = int(input(f"Escolha sua classe {jogador}! "))

        if escolha in [1, 2, 3]:
            #Com "if" atribuímos a classe correta (com o índice - 1, então cabe 0, 1, 2), com o jogador determinado
            if jogador == "Jogador 1":
                stats_jogador1 = classes[escolha - 1]

            else:
                stats_jogador2 = classes[escolha - 1]

            print(f"{jogador} escolheu ser um {'Guerreiro' if escolha == 1 else 'Mago' if escolha == 2 else 'Ladino'}.")

            #Para sair do loop se as classes escolhidas estiverem corretas
            break

        #Se a entrada for inválida, permite que a classe seja solicitada novamente
        else:
            print("Número inválido, escolha uma classe entre 1, 2 ou 3.")


#Função para definir o sistema de batalha do jogo
def batalha(vida_jogador1, stats_jogador1, vida_jogador2, stats_jogador2):
    #Criamos uma variável auxiliar para controlar a quantidade de turnos do jogo
    turno = 0

    #Define os estados de defesa iniciais
    defesa_jogador1 = False
    defesa_jogador2 = False

    #Definir a vida dos jogadores, segundo o valor nas listas
    vida_jogador1 = stats_jogador1[0]
    vida_jogador2 = stats_jogador2[0]
    #Define que a poção não foi usada por nenhum jogador
    pocao_usada_jogador1 = False
    pocao_usada_jogador2 = False

    #Loop "While" mantém o jogo em loop e os turnos em andamento até que uma das vidas do jogador chegue a 0
    while vida_jogador1 > 0 and vida_jogador2 > 0:
        turno += 1

        #Informar o turno do jogo e a vida de ambos os jogadores
        print(f"TURNO {turno}.")
        print(f"Jogador 1 está com {vida_jogador1} de vida.")
        print(f"Jogador 2 está com {vida_jogador2} de vida.")

        #Loop dos turnos dos jogadores
        for jogador in range(1, 3):
            if jogador == 1:
                escolha = int(input("Jogador 1, digite 1 para atacar, 2 para defender ou 3 para usar um item: "))
                stats = stats_jogador1
                vida_atual = vida_jogador1

            else:
                escolha = int(input("Jogador 2, digite 1 para atacar, 2 para defender ou 3 para usar um item: "))
                stats = stats_jogador2
                vida_atual = vida_jogador2

            #Se a escolha for defesa
            if escolha == 2:
                #Dado de 20 lados, onde, com a ajuda de "randomint", nos dá um número inteiro aleatório
                dado = random.randint(1, 20)
                print(f"A rolagem do dado resultou em: {dado}.")

                #A chance de defesa depende da defesa maxima do jogador
                if dado >= stats[4]:
                    if jogador == 1:
                        defesa_jogador1 = True
                        print(f"O jogador 1 está defendendo! Só receberá metade do dano.")
                    else:
                        defesa_jogador2 = True
                        print(f"O jogador 2 está defendendo! Só receberá metade do dano.")
                else:
                    if jogador == 1:
                        defesa_jogador1 = False
                        print("O jogador 1 falhou na defesa!")
                    else:
                        defesa_jogador2 = False
                        print("O jogador 2 falhou na defesa!")

            #Se a escolha for ataque
            elif escolha == 1:
                #Dado de 20 lados, de novo
                print(f"O Jogador {jogador} decidiu atacar.")
                dado = random.randint(1, 20)
                print(f"A rolagem do dado resultou em: {dado}.")

                #Com o índice “3” acessamos o acerto minimo com o "1" acessamos o dano minimo, e com o "2" acessamos o dano maximo
                if dado >= stats[3]:
                    #Se o dado estiver acima do mínimo, mas não 20, então o dano é a média do dano máximo e mínimo do jogador
                    dano = (stats[1] + stats[2]) // 2

                    #Se o dado for 20, sendo um acerto crítico, então é o dano máximo
                    if dado == 20:
                        dano = stats[2]

                    #Se algum dos jogadores se defender, o dano que toma se tem que dividir
                    if jogador == 1 and defesa_jogador2:
                        dano = dano // 2
                        print("A defesa reduz o dano tomado por Jogador 2 pela metade!")

                    elif jogador == 2 and defesa_jogador1:
                        dano = dano // 2
                        print("A defesa reduz o dano tomado por Jogador 1 pela metade!")

                    if jogador == 1:
                        vida_jogador2 -= dano
                        print(f"O Jogador 2 recebeu {dano} de dano e está com {vida_jogador2} de vida!")

                    else:
                        vida_jogador1 -= dano
                        print(f"O Jogador 1 recebeu {dano} de dano e está com {vida_jogador1} de vida!")

                #Se o dado estiver abaixo do mínimo, o acerto é um erro e o dano é 0
                else:
                    if jogador == 1:
                        print(f"Ataque errou! A vida do jogador 2 não é afetada.")

                    else:
                        print(f"Ataque errou! A vida do jogador 1 não é afetada.")

            #Se a escolha for um item
            elif escolha == 3:
                print(f"jogador {jogador} decidiu utilizar um item, digite 1 para usar a poção (apenas um uso) ou digite qualquer outra coisa para cancelar.")
                escolha_item = (input(""))
                if int(escolha_item) == 1:
                    if jogador == 1:
                        if not pocao_usada_jogador1:
                            vida_jogador1 += 10
                            pocao_usada_jogador1 = True
                            print(f"O Jogador 1 foi curado, sua vida atual agora é: {vida_jogador1}")

                        else:
                            print("O Jogador 1 já usou a poção!")

                    elif jogador == 2:
                        if not pocao_usada_jogador2:
                            vida_jogador2 += 10
                            pocao_usada_jogador2 = True
                            print(f"O Jogador 2 foi curado, sua vida atual agora é: {vida_jogador2}")

                        else:
                            print("O Jogador 2 já usou a poção!")

                else:
                    continue

    #Condição para encerrar o jogo, informar o vencedor, se a vida de alguém for menor ou igual a 0
    if vida_jogador1 <= 0:
        print("Jogador 2 venceu!")
        print("Obrigado por jogar 'Encontro das Sombras'! Esperamos que tenha se divertido!")

    elif vida_jogador2 <= 0:
        print("Jogador 1 venceu!")
        print("Obrigado por jogar 'Encontro das Sombras'! Esperamos que tenha se divertido!")


#Função do jogo final
def jogo():
    escolher_classe("Jogador 1")
    escolher_classe("Jogador 2")
    batalha(vida_jogador1, stats_jogador1, vida_jogador2, stats_jogador2)


#Usando a função para iniciar o jogo
jogo()
