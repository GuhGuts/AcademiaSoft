print("INICIO")

a = int(input("Pontos do jogador A: "))
b = int(input("Pontos do jogador B: "))
c = int(input("Pontos do jogador C: "))

if a > b and a > c:
    print("Jogador A venceu!")
elif b > a and b > c:
    print ("Jogador B venceu!")
elif c > a and c > b:
    print("Jogador C venceu!")
elif a >= b or a >= c:
    print("Houve um empate, jogue novamente")
elif b >= a or b >= c:
    print("Houve um empate, jogue novamente")
elif c >= a or c >= b:
    print("Houve um empate, jogue novamente")


print("FIM")