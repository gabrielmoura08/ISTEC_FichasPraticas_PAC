print("_____FP 02 | EX 09_____")

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
num3 = int(input("Insira outro número: "))

if  num1 < num2 < num3:
    print(f"Menor: {num1}")

if  num2 < num1 < num3:
    print(f"Menor:{num2}")

if  num3 < num1 < num2:
    print(f"Menor:{num3}")


