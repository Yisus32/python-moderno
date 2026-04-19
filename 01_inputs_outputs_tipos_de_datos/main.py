#inputs y outputs
peso = float(input("Ingrese su peso"))
altura = float(input("Ingrese su altura"))

imc = peso / (altura ** 2)

print("El imc es de: " + str(imc))

if imc < 18.5:
    print("IMC Bajo (Desnutricion)")
if imc >= 18.25 and imc <= 25:
    print("IMC es normal")
if imc > 25:
    print("IMC es alto (Obesidad)")