import random

def imprime_mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

def carrega_palavra_secreta():
    arquivo_palavras = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo_palavras:
        linha = linha.strip()
        palavras.append(linha)

    arquivo_palavras.close()

    numero_random = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_random].strip().lower()

    return palavra_secreta
    
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_letra():
    letra_chutada = input("Digita uma letra: ")
    return letra_chutada.strip().lower()

def marca_letra_correta(letra_chutada, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if( letra == letra_chutada ):
            # print(f'letra {letra} encontrada na posicao {index}')
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar() :
    
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    numero_erros = 0

    print(letras_acertadas)
    while( not enforcou and not acertou  ):
        letra_chutada = pede_letra()

        if( letra_chutada in palavra_secreta ):
            marca_letra_correta(letra_chutada, letras_acertadas, palavra_secreta)
        else:
            numero_erros += 1
            desenha_forca(numero_erros)
        
        enforcou = numero_erros >= 7
        if( '_' not in letras_acertadas ):
            acertou = True
        
        print(letras_acertadas)
    
    if( enforcou ):
        imprime_mensagem_perdedor(palavra_secreta)
    else:
        imprime_mensagem_vencedor()


if( __name__ == "__main__"):
    jogar()