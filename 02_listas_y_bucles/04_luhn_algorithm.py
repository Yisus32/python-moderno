numero = str(input("Ingrese ultimos 4 digitos de la TC: "))

invertido = numero[::-1]

multi = 0

suma = 0

for valor, index in enumerate(invertido):
    print(valor, index)

    i = int(index) + 1;

    if i % 2 != 0:
        multi = int(valor) * 2
    
    if multi > 9:
        multi -= 9

    suma += multi

if suma % 10 == 0:
    print("El numero es valido")
else:
    print("El numero es invalido")   