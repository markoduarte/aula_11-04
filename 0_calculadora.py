valor1 = int(input())
operador = input()
valor2 = int(input())
while (valor1 > 0 and valor2 > 0):
    if operador == '+':
        resultado = (valor1 + valor2)
        print(resultado)
        
    elif operador == '-':
        resultado = (valor1 - valor2)
        print(resultado)
                    
    elif operador == '*':
        resultado = (valor1 * valor2)
        print(resultado)
        
    elif operador == '/':
        resultado = (valor1 / valor2)
        print(resultado)
               
    else:
        print('operador inválido')

    valor1 = int(input())
    operador = input()
    valor2 = int(input())
        
print("programa encerrado!")