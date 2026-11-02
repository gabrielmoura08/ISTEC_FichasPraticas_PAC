print("_____FP 03 | EX 15_____")

num  = int(input("Introduza um número inteiro não-negativo: "))

fatorial = 1
i = num
expressao = ""

while i > 1:
    fatorial *= i
    expressao += f"{i}x"
    i -= 1

expressao += "1"

print(f"Fatorial de {num}: {expressao}={fatorial}")
