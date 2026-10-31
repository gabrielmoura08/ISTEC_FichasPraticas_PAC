print("_____FP 03 | EX 14_____")

n = int(input("Quantos números deseja inserir: "))

crescente = True
anterior = None

for i in range(n):
    numero = int(input("Introduza um número: "))
    if anterior is not None and numero < anterior:
        crescente = False
    anterior = numero

if crescente:
    print("Crescente")
else:
    print("Não crescente")