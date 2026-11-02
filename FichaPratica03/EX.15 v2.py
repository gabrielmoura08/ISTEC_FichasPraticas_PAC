print("_____FP 03 | EX 15 v2_____")

num = int(input("Introduza um número inteiro não-negativo: "))

fatorial = 1
i = num
expressao = ""

while i > 1:
    novo = 0
    contador = 0
    while contador < i:
        novo += fatorial
        contador += 1
    fatorial = novo

    expressao += f"{i}x"
    i -= 1

expressao += "1"

print(f"Fatorial de {num}: {expressao}={fatorial}")