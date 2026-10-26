print("_____FP 02 | EX 02_____")

salario = float(input("Insira o seu salário anual: "))

# 2 Taxas
taxa20 = salario * 0.2
taxa30 = salario * 0.3

if salario <= 15000:
    print(f"Paga taxa de 20%: {taxa20} € ")
else:
    print(f"Paga taxa de 30%: {taxa30} € ")



