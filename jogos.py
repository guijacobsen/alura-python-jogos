import forca;
import adivinha_numero;

print("*******************")
print("Escolha o seu jogo!")
print("*******************")


print("(1) Forca (2) Adivinhacao")
jogo_escolhido = int(input("Qual o jogo? "))

if( jogo_escolhido == 1 ):
    forca.jogar()
elif( jogo_escolhido == 2 ):
    adivinha_numero.jogar()
else:
    print("Jogo invalido")