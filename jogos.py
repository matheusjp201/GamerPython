import forca
import adivinhacao
import velha_

def escolha_seu_jogo():
    print("Escolha seu jogo e venha se divertir ! ")
    print("(1) Forca (2) Adivinhação (3) Jogo da Velha")

    jogo = int(input("Qual jogo você quer jogar?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    
    if(jogo == 3):
        print("Jogo da Velha")
        velha_.jogar()

if(__name__ == "__main__"):
    escolha_seu_jogo()