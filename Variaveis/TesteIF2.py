valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
tipo = input("Funcao (+, -, *, /) : ")

if(tipo == '+'):
    print("Soma: ",valor1 + valor2)
elif(tipo == '-'):
    print("Subtração", valor1 - valor2)
elif(tipo == '*'):
    print("Multiplicação", valor1 * valor2)
elif(tipo == '/'):
    print("Divisão", valor1 / valor2)