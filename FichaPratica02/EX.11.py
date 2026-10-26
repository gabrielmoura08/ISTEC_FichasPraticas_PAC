print("_____FP 02 | EX 11_____")

saldo = float(input(f"Introduza saldo médio: "))
montante = float(input(f"Introduza o valor a movimentar: "))

saldo = saldo + montante

print(f"Saldo Atual: {saldo}")

if saldo <= 0:
    print(f"Operação Inválida. Saldo Insuficiente.")

    

