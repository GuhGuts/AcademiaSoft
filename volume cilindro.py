#Faça um programa que calcule o volume de um cilindro area = raio * raio * 3.14 volume = area * altura

raio = float(input("Digite o raio: "))
altura = float(input("Digite a altura: "))

area = raio * raio * 3.14
volume = area * altura

print("O volume do seu cilindro é de: {}m³".format(volume))