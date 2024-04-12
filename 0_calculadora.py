def soma(valor1,valor2):
    return valor1 + valor2
def subt(valor1,valor2):
    return valor1 - valor2
def mult(valor1,valor2):
    return valor1 * valor2
def div(valor1,valor2):
    return valor1 / valor2

valor1 = int(input())
operador = input()
valor2 = int(input())

while (valor1 > 0 and valor2 > 0):
    if operador == '+':
        print(soma(valor1,valor2))

    elif operador == '-':
        print(subt(valor1,valor2))
                    
    elif operador == '*':
        print(mult(valor1,valor2))
        
    elif operador == '/':
        print(div(valor1,valor2))
               
    else:
        print('operador inválido')

    valor1 = int(input())
    operador = input()
    valor2 = int(input())
        
print("programa encerrado!")