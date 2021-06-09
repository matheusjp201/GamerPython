import random

def jogos():
    

    print("Jogo da adivinhação ! ")


    numero_da_sorte = random.randrange(1, 21) 
    total_de_tentativas = 0
    pontos = 100

    print("Qual nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil ")

    nivel = int(input("Defina o seu nível de dificuldade: "))

    if(nivel == 1):
        total_de_tentativas = 10

    elif(nivel == 2):
        total_de_tentativas = 7

    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute_str = input("Tente a sorte, Digite um número entre 1 a 20: ")

        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 20):
            print("Você deve digitar um número entre 1 e 20 ")
            continue

        acertou = chute == numero_da_sorte
        maior = chute > numero_da_sorte
        menor = chute < numero_da_sorte

        if(acertou):
            print("Você acertou o numero da sorte  e fez {} pontos!".format(pontos))
            break

        else:
            pontos_perdidos = abs(numero_da_sorte - chute) #pontos perdidos na rodada
            pontos = pontos - pontos_perdidos #subtraindo os pontos perdidos

            if(maior):
                print("O seu número foi maior que o número da sorte ")
                if (rodada == total_de_tentativas):
                    print("O número da sorte era {}. Você fez {}".format(numero_da_sorte, pontos))
            
            elif(menor):
                print("Você errou ! O seu número foi menor do que o número da sorte ")
                if(rodada == total_de_tentativas):
                    print("O número da sorte era {}. Você fez {}".format(numero_da_sorte))
    

    print("Fim de Jogo ")

if(__name__ == "__main__"): 
    jogos()
