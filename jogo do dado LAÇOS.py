from random import randint

print("Bem-vindo ao JOGO DOS DADOS")
print("Para sair, pressione a tecla 9 \n")
a = 1

while a == 1:
    cpu = randint(1, 6)

    num = int(input("\nDigite um numero de 1 a 6: "))

    if num == 9:
        a = 0

    print("O numero que vc escolheu foi: ", num)
    print("O numero sorteado no dado foi: ", cpu)

    if cpu == num:
        print("Você ganhou, Parabéns :)")
        a = 0
        again = input("\nJogar novamente? [s/n] ")
        if again == ("s"):
            a = 1
        else:
            print("Fim de jogo.")


    else:
        print("Que pena, você perdeu, tente de novo :(\n\n")






