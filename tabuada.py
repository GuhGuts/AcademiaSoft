print("TABUADA\n")

n = int(input("Digite um numero para calcular a tabuada: "))
a = int(input("Até qual nivel da tabuada voce quer ver? \n"))


for x in range(1, a + 1, 1):
    print("{}x{} = {}".format(n, x, n * x))
    x = x + 1
