import forca
import adivinhacao

def escolha_seu_jogo():
    print("Escolha seu jogo e venha se divertir ! ")
    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogos()

    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogos()

if(__name__ == "__main__"):
    escolha_seu_jogo()