print("_____FP 04 | EX 4_____")

#1. Perguntar os números

repertir = "s"

#2. Contas
while repertir == "s":
    num1 = int(input("Introduza um número: "))
    num2 = int(input("Introduza outro número: "))
    caracter = (input("Introduza um caracter ( + - * / ): "))

    if caracter =="-":
        sub = num1 - num2
        print(f"{sub}")

    elif caracter == "+":
        soma = num1 + num2
        print(f"{soma}")

    elif caracter == "*":
        multi = num1 * num2
        print(f"{multi}")

    elif caracter == "/":
        div = num1 / num2
        print(f"{div}")

    repertir = input("Deseja continuar? (introduza s/n): ")








