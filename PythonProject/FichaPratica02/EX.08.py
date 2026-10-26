print("_____FP 02 | EX 08_____")

nota1 = float(input("Insira a nota 1 (0-20): "))
nota2 = float(input("Insira a nota 2 (0-20): "))
nota3 = float(input("Insira a nota 3 (0-20): "))

media = nota1 * 0.25 + nota2 * 0.35 + nota3 * 0.40

print(f"Média final: {media:.2f}")

if media > 9.5:
    print("Aprovado")
else:
    print("Não aprovado")