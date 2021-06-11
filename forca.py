def jogar():
    print("Jogo da forca ! ")

    palavra_escondida = "Astronauta"
    enforcou = False
    acertou = False

#enquanto(True e não True)
    while(not enforcou and not acertou):

        chute = input("Qual a letra que você deseja escolher? ")
        chute = chute.strip()

        index = 0
        
        for letra in palavra_escondida:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
            
        
        
        print("Vamos continuar jogando")


    print("Fim de Jogo ")


if(__name__ == "__main__"):
    jogar()