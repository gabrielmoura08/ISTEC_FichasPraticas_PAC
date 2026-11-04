print("_____FP 04 | EX 8_____")

numero = int(input("Insira um número: "))

soma = 0
i = 1

while soma < numero:
    soma = soma + i
    i = i + 1

if soma == numero:
    print("O número é triangular!")
else:
    print("O número não é triangular!")