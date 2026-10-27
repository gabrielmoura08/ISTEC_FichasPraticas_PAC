print("_____FP 03 | EX 11_____")

limite = int(input("Introduza o Limite: "))
salto = int(input("Introduza o Salto: "))

for i in range(0, limite + 1, salto):
    print(i, end=" ")
print()