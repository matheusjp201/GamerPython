print("Bem vindo ao jogo de adivinhação ! ")


numero_da_sorte = 16
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    chute_str = input("Tente a sorte, Digite seu número:")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_da_sorte
    maior = chute > numero_da_sorte
    menor = chute < numero_da_sorte

    if(acertou):
        print("Você acertou o numero secreto !")

    else:
        if(maior):
            print("Você errou ! O seu chute foi maior do que número da sorte")
        elif(menor):
            print("Você errou ! O seu número foi menor do que o número da sorte")

print("Fim de Jogo ")