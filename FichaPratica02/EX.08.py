print("_____FP 02 | EX 08_____")

nota1 = float(input("Insira uma nota: "))
nota2 = float(input("Insira outra nota: "))
nota3 = float(input("Insira outra nota: "))

#2. Média
media =( nota3+nota1+nota2)/3

print(f"Média: {media}")

if media >= 9.5:
    print(f"Aprovado")
else:
    print(f"Reprovado")