a = int(input("\nDigite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite mais um numero: "))

if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
else:
    print(c, b, a)
