import math as m
peso = float(input('Qual é o seu peso ?'))
altura = float(input('qual é a sua altura?'))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc}')