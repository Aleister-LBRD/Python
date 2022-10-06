# calculadora ORIENTADA A OBJETOS

# definindo classe
class calculadora ():
    def __init__(self,num1,num2,op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
    
    def calculo(self):
        if self.op == '+':
            return self.num1 + self.num2
        if self.op == '-':
            return self.num1 - self.num2
        if self.op == '*':
            return self.num1 * self.num2
        if self.op == '/':
            return self.num1 / self.num2
        else: 
            print('Opção invalida')
            return False

    def resultado(self):
        return print(f'{self.num1} {self.op} {self.num2} = {self.calculo()}')

# main
def main():
    num1 = int(input('Insira o primeiro elemento: '))
    num2 = int(input('Insira o segundo elemento: '))
    op = input('Insira o operador: ')
    calc = calculadora(num1,num2,op)

    if calc.calculo() != False:
        calc.calculo()
        calculadora(num1,num2,op).resultado()
    else:
        print('Tente novamente')

# executando
if __name__ == '__main__':
    main()


