print("_____FP 02 | EX 10_____")

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

operacao = input(f"Escolha a operação que quer usar ( + - * / ): ")

if operacao == "+":
    soma = num1 + num2
    print(f"Soma: {soma}")

elif operacao == "-":
    subtracao = num1-num2
    print(f"Subtração: {subtracao}")

elif operacao == "*":
    multiplicacao = num1 * num2
    print(f"Multiplicação: {soma}")

elif operacao == "/":
    divisao = num1 / num2
    print(f"Divisão: {divisao}")

else:
    print(f"Erro: {operacao} não reconhecido")




