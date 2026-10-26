print("_____FP 02 | EX 15_____")


a = int(input("Insira um número: "))
b = int(input("Insira outro número: "))
c = int(input("Insira outro número: "))

ordem = input(f"Escolha a ordem Crescente C ou Decrescente D: ")


if ordem == "C":
    if a <= b <= c:
        print(f"{a} {b} {c}")
    elif a <= c <= b:
        print(f"{a} {c} {b}")
    elif b <= a <= c:
        print(f"{b} {a} {c}")
    elif b <= c <= a:
        print(f"{b} {c} {a}")
    elif c <= a <= b:
        print(f"{c} {a} {b}")
    else:
        print(f"{c} {b} {a}")

elif ordem == "D":
    if a >= b >= c:
        print(f"{a} {b} {c}")
    elif a >= c >= b:
        print(f"{a} {c} {b}")
    elif b >= a >= c:
        print(f"{b} {a} {c}")
    elif b >= c >= a:
        print(f"{b} {c} {a}")
    elif c >= a >= b:
        print(f"{c} {a} {b}")
    else:
        print(f"{c} {b} {a}")

else:
    print("Opção inválida. Escolha C ou D.")