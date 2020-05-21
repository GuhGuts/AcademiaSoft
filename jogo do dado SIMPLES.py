from random import randint

print("Bem vindo ao JOGO DO DADO\n")

cpu = randint(1, 6)

num = int(input("Digite um numero de 1 a 6: "))

print("O numero que vc escolheu foi: ", num)
print("O numero sorteado no dado foi: ", cpu)

a = bool(cpu == num)

print("Você ganhou:", a)

print("Fim de jogo.")
