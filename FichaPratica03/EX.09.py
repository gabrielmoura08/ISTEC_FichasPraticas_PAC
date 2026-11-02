print("_____FP 03 | EX 9_____")

soma = 0
contador = 0
numero = float(input("Introduza um número (-1 para terminar): "))

while numero != -1:
    numero = float(input("Introduza um número (-1 para terminar): "))
    if numero !=-1:
        soma = soma + numero
        contador = contador + 1
        media = soma / contador

print("Média:", media)

