print("_____FP 04 | EX 7_____")

numero = int(input("Insira um número: "))

divisores = 0
contador = 1

while contador <= numero:

    if numero % contador == 0:
        divisores = divisores + 1

    contador = contador + 1

if divisores == 2:
    print("O número é primo")

else:
    print("O número não é primo")
