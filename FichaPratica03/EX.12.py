print("_____FP 03 | EX 12_____")

c1 = c2 = c3 = c4 = 0

n = int(input("Número: "))

while n >= 0:
    if n <= 25:
        c1 += 1
    elif n <= 50:
        c2 += 1
    elif n <= 75:
        c3 += 1
    elif n <= 100:
        c4 += 1
    n = int(input("Número: "))

print("[0,25]:", c1)
print("[26,50]:", c2)
print("[51,75]:", c3)
print("[76,100]:", c4)