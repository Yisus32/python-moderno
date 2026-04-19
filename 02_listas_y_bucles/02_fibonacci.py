longitud = int(
    input("Ingrese la longitud de la cadena: ")
)

terminoPrimario = 0;
terminoSecundario = 1;

terminoResultante = terminoPrimario + terminoSecundario


fibonacci = []

for i in range(longitud):
    if i == 0:
        fibonacci.insert(i, terminoPrimario)
    if i == 1:
        fibonacci.insert(i, terminoSecundario)
    if i > 1:
    
        fibonacci.insert(i, terminoResultante)

        terminoPrimario = terminoSecundario
        terminoSecundario = terminoResultante

        terminoResultante = terminoPrimario + terminoSecundario

#Longitud usando el valor de entrada
print("La longitud es (usando valor de entrada): ", longitud)

#Longitud usando la funcion len
print("La longitud es (usando funcion len() ): ", len(fibonacci))

#longitud usando un contador
contador = 0

contadorPares = 0

for i in fibonacci:
    contador+=1

    if int(i) % 2 == 0:
        contadorPares+=1

#Longitud usando la funcion len
print("Fibonacci: ", fibonacci)
print("La longitud es (usando un contador): ", contador)
print("Cantidad de pares: ", contadorPares - 1 )
print("Cantidad impares: ", contador - (contadorPares - 1) - 1)