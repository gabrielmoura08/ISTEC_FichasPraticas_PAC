print("_____FP 03 | EX 9_____")

soma = 0
contador = 0

numero = float(input("Introduza um número (-1 para terminar): "))

while numero != -1:
    soma += numero
    contador += 1
    numero = float(input("Introduza um número (-1 para terminar): "))

if contador > 0:
    media = soma / contador
    print(f"A média dos números introduzidos é: {media:.2f}")
else:
    print("Não foram introduzidos números.")