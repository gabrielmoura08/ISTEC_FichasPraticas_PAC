print("_____FP 02 | EX 09_____")

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
num3 = int(input("Insira outro número: "))

if num1 <= num2:
    if num1 <= num3:
        print(f"{num1}")
    else:
        print(f"{num3}")
else:
    if num2 <= num3:
        print(f"{num2}")
    else:
        print(f"{num3}")