numero = str(input("Ingrese un numero: "))

#1 Determinar la cantidad de cifras del numero
cifras = len(numero)

suma = 0

#Separar numero en cada valor
for i in numero:
    suma += pow(int(i), cifras)

print("Numero original: ", numero)
print("Numero con Amstrong: ", suma)  

if int(numero) == int(suma): 
    print("El numero ingresado es un numero de Amstrong")
else:
    print("El numero ingresado no es un numero de Amstrong")
