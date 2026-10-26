print("_____FP 02 | EX 13_____")

horas = int(input(f"Introduza as horas: "))
minutos = int(input(f"Introduza os minutos: "))

periodo = "PM" if horas >= 12 else "AM"

horas12 = horas % 12
if horas == 0:
    horas12 = 12

print (f"{horas12}:{minutos:02d} {periodo}")