print("_____FP 03 | EX 13_____")

#Pedir os números
num1 = int(input("Início: "))
num2 = int(input("Fim: "))

#percorrer o intervalo inicio numero x e fim numero y o + 1 é adicionar + 1 ao num dito pelo utilizador
for i in range(num1, num2 + 1):

    # : filtrar os múltiplos de 5
    if i % 5 == 0:
        print(i)
