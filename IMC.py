print("Vamos calcular o IMC")
peso = float(input("Digite o seu peso:\n"))
altura = float(input("Digite a sua altura:\n"))
imc = peso / (altura * altura)

print(round(imc, 2))

if imc >= 25:
    print('gordo')

elif imc >=18 and imc < 25:
    print('ok')

else:
    print('magrão')

