print("_____FP 02 | EX 10_____")

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Insira a operação (+, -, *, /): ")

valida = True

if operacao == "+":
    resultado = num1 + num2
if operacao == "-":
    resultado = num1 - num2
if operacao == "*":
    resultado = num1 * num2
if operacao == "/":
    resultado = num1 / num2

if operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/":
    valida = False

if valida:
    print(f"Resultado: {resultado}")
else:
    print("Erro: operação inválida")