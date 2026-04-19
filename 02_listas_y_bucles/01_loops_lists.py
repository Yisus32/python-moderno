#lista
imcs = [29, 30, 20, 39, 59, 39]

#bucle for
for i in range(len(imcs)):
    if imcs[i] < 18.5:
        print("IMC Bajo (Desnutricion)")
    if imcs[i] >= 18.25 and imcs[i] <= 25:
        print("IMC es normal")
    if imcs[i] > 25:
        print("IMC es alto (Obesidad)")

obesos = [o for o in imcs if o > 25]
normales = [n for n in imcs if (n >= 18.25 and n <= 25)]

print("Obesos:", obesos)
print("Normales:", normales)