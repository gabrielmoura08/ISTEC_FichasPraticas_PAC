print("_____FP 03 | EX 13_____")


limite = int(input("Introduza o Limite: "))
salto = int(input("Introduza o Salto: "))

numero = 0

while numero <= limite:
    if numero % 5 == 0:
        print(numero)
    numero = numero + salto