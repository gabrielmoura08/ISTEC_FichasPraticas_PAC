print("_____FP 01 | EX 05_____")

#1.Pedir os números

num1 = float(input("Insira a nota 1: "))
num2 = float(input("Insira a nota 2: "))
num3 = float(input("Insira a nota 3: "))

#2. Média
media =( num3+num1+num2)/3
percentagem1 = num1*0.2
percentagem2 = num2*0.3
percentagem3 = num3*0.5

media2 = (percentagem1+percentagem2+percentagem3)/3

#3. Resultado

print(f"Resultado da média aritmetica: {media}")
print(f"Resultado da percentagem: {media2}")


