print("_____FP 01 | EX 08_____")

# 1 Perguntar ao utilizador

musica1min = int(input("Introduza os segundos da música 1: "))
musica1seg = int(input("Introduza os minutos da música 1: "))

musica2min = int(input("Introduza os segundos da música 2: "))
musica2seg = int(input("Introduza os minutos da música 2: "))

musica3min = int(input("Introduza os segundos da música 3: "))
musica3seg = int(input("Introduza os minutos da música 3: "))

musica4min = int(input("Introduza os segundos da música 4: "))
musica4seg = int(input("Introduza os minutos da música 4: "))

musica5min = int(input("Introduza os segundos da música 5: "))
musica5seg = int(input("Introduza os minutos da música 5: "))

totalSegundos = musica1seg + (musica1min*60) + musica2seg + (musica2min*60) + musica3seg + (musica3min*60) + musica4seg + (musica4min*60) + musica5seg + (musica5min*60)

# 2 Calculos

horas = totalSegundos // 3600
totalSegundos = totalSegundos % 3600

minutos = horas // 60
totalSegundos = totalSegundos % 60

segundos = horas - minutos

# 3 Total de segundos do albúm
print(f"Total Álbum: {horas}h {minutos}m {segundos}s")






