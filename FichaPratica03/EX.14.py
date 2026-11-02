print("_____FP 03 | EX 14_____")

n = int(input("Quantos números deseja inserir: "))

crescente = True
anterior = None
i = 0

while i < n:
    numero = int(input("Introduza um número: "))
    if anterior is not None and numero < anterior:
        crescente = False
    anterior = numero
    i += 1

if crescente:
    print("Crescente")
else:
    print("Não crescente")