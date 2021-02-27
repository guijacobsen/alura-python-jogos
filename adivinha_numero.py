def jogar() :
    import random;
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")

    print('\Escolher niveis do jogo')
    print('(1) Facil (2) Medio (3) Dificil')

    nivel = int(input('Qual nivel? '))
    numero_secreto = random.randrange(1,101)

    pontos = 1000

    if( nivel == 1 ):
        total_tentativas = 20
    elif( nivel == 2 ):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for i in range(0, total_tentativas) :
        print("\nTentativa {} de {}".format(i, total_tentativas))
        numero_chute = int(input("Chute um numero entre 1 e 100: "))

        numero_chute = abs(numero_chute)

        if( numero_chute < 1 or numero_chute > 100):
            pontos = pontos - 10
            print('Numero deve ser entre 1 e 100')
            continue

        if( numero_secreto == numero_chute ):
            print("**********\nVc acertou\n**********\nPontos: ", pontos)
            break
        else:
            if(numero_chute > numero_secreto) :
                print("Errou!! Seu numero eh maior que o numero secreto")
                pontos = pontos - (numero_chute  - numero_secreto)
            else:
                print("Errou!! Seu numero eh menor que o numero secreto")
                pontos = pontos - (numero_secreto - numero_chute)


if( __name__ == "__main__"):
    jogar()