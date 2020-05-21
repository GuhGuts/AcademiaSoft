cartas = int(input("Digite a soma das cartas que vc tem na mão: "))

if (cartas <= 10):
    print("Sem duvida, compre mais uma carta.")
elif (cartas > 10) and (cartas <= 15):
    print("Há um risco, mas aconselho a comprar mais uma carta.")
elif (cartas > 15) and (cartas <= 20):
    print("Aconselho a parar de jogar.")
elif (cartas==21):
    print("Você ganhou, não compre mais nada!")
elif(cartas > 21):
    print("Você perdeu")