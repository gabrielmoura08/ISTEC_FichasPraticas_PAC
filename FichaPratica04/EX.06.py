print("_____FP 04 | EX 6_____")

j1 = int(input("Jogador 1 insira um número: "))
j2= int(input("Jogador 2 tente adivinhar o número escolhido pelo jogador 1: "))

tentativas = 1

while j2 != j1:

    if j2 < j1:
        print("O número é superior")

    else:
        print("O número é inferior")

    j2 = int(input("Jogador 2 tente adivinhar novamente: "))
    tentativas = tentativas + 1

print("Parabéns Acertou!")
print(f"Número de tentativas:",tentativas)
