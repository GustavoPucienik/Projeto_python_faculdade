import math as m
peso = float(input('Qual é o seu peso ?'))
altura = float(input('qual é a sua altura?'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você esta abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você esta no peso ideal.')
elif 25 <= imc:
    print('Você esta em sobrepeso.')
print('O seu IMC é {:.2f}'.format(imc))
