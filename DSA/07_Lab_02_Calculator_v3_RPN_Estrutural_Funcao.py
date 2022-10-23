# Calculadora ESTRUTURAL COM FUNÇÕES

print("**********Python Calculator**********")

num1 = int(input('Insira o primeiro elemento: '))
num2 = int(input('Insidera o segundo elemento: '))
operador = input('Insira a operação: ')

# funcoes
def soma (num1,num2):
    return num1 + num2

def sub (num1,num2):
    return num1 - num2

def div (num1,num2):
    return num1 / num2

def mult (num1,num2):
    return num1 * num2

if operador == '+':
    print(f'{num1} {operador} {num2} = {soma(num1,num2)}')
if operador == '-':
    print(f'{num1} {operador} {num2} = {sub(num1,num2)}')
if operador == '*':
    print(f'{num1} {operador} {num2} = {mult(num1,num2)}')
if operador == '/':
    print(f'{num1} {operador} {num2} = {div(num1,num2)}')

