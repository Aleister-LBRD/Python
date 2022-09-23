# Calculadora em Python

print("**********Python Calculator**********\n\nSeleciona o numero da operação desejada:")

print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

operacao = int(input ("Digite sua opção (1/2/3/4):"))
num1 = int(input ("Digite o primeiro numero:"))
num2 = int(input ("Digite o segundo numero:"))
resultado = 0


if operacao == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == 2:
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == 3:
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
else:
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")
