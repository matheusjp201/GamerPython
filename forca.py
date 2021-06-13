import random

def jogar():
    imprime_mensagem_abertura()
    palavra_escondida = carrega_palavra_escondida()

    letras_acertadas = inicializa_letras_acertadas(palavra_escondida)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0


    while(not enforcou and not acertou):

        chute = um_chute()

        if(chute in palavra_escondida):
            chute_correto(chute, letras_acertadas, palavra_escondida)
        else:
            tentativas += 1
            desenho_da_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
    
    if("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
        
    else:
        imprime_mensagem_perdedor(palavra_escondida)
    


def desenho_da_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(tentativas == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(tentativas == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (tentativas == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_escondida):
    print("Poxa, você foi enforcado hahahah!")
    print("A palavra certa era {}".format(palavra_escondida))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄") 
    print("████▌▄▌▄▐▐▌█████") 
    print("████▌▄▌▄▐▐▌▀████") 
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀") 

def chute_correto(chute, letras_acertadas, palavra_escondida):
    index = 0
    for letra in palavra_escondida:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def um_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_mensagem_abertura():
    print("+--------------------------------+")
    print("+++Bem vindo ao jogo da Forca!++++")
    print("+--------------------------------+")

def carrega_palavra_escondida():
    arquivo = open("palavras.md", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_escondida = palavras[numero].upper()
    return palavra_escondida


if(__name__ == "__main__"):
    jogar()