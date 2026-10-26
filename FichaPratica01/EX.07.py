print("_____FP 01 | EX 07_____")

# 1 Perguntar os valores ao Utilizador
preco1 = float(input("Insira o preco do 1º produto: "))
preco2 = float(input("Insira o preco do 2º produto: "))
preco3 = float(input("Insira o preco do 3º produto: "))
preco4 = float(input("Insira o preco do 4º produto: "))

# 2 Calcular o valor total
total = preco1 + preco2 + preco3

# 3 Aplicar o desconto

precoDesconto = total * 0.9

# 4 Apresentar os resultados
print(f"Preço com os 10% de desconto: {precoDesconto}")
