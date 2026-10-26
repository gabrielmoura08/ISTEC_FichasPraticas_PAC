print("_____FP 02 | EX 11_____")

saldo = float(input("Introduza saldo médio: "))
montante = float(input("Introduza valor a movimentar: "))

saldo_final = saldo + montante

if saldo_final >= 0:
    saldo = saldo_final
else:
    print("Operação Inválida. Saldo Insuficiente.")

print(f"Saldo Atual: {saldo}")

