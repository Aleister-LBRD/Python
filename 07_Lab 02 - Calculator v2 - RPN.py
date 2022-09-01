# Calculadora em Python

print("**********Python Calculator**********")

num1 = int(input ("Digite o primeiro numero:"))
num2 = int(input ("Digite o segundo numero:"))
operacao = input ("Digite a operação (+,-,*,/)")
resultado = 0

if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")
else:
    print("opção invalida!")