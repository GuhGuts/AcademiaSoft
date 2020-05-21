from random import randint

print("Bem vindo ao JOGO DO DADO\n")

cpu = randint(1, 6)

str_num = input("Digite um numero de 1 a 6: ")

num = int(str_num)

print("O numero que vc escolheu foi: ", num)
print("O numero sorteado no dado foi: ", cpu)


if cpu == num:
    print("Você ganhou, Parabéns :)")
else:
    print("Que pena, você perdeu :(")

print("Fim de jogo.")