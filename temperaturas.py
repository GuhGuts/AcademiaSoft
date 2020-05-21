#Faça um programa conversor de temperatura, que receba a temperatura em graus Celsius e converta-a para Fahrenheit
# Formula : Tf = (9/5) * Tc + 32
# Desafio: Converta o número para graus Kelvin também

tc = int(input("\nQuantos graus esta agora? "))

tf = (9/5) * tc + 32
tk = tc + 273.15

print("A temperatura em Celsius é:", tc, "ºC")
print("A temperatura em Fahrenheit é:", tf, "ºF")
print("A temperatura em Kelvin é:", tk, "K")
