# print('1. soma')
# print('2. multiplicação')
# print('3. divisão')
# print('4. soma')

operacao = input('digite a opção desejada (1/2/3/4): ')

num1 = float(input('digite o primeiro numero: '))
num2 = float(input('digite o valor do segundo numero: '))

if operacao == '1' or operacao == '4':
    if operacao == '4':
        resultado = num1-num2
        print (num1, "-", num2, "=", resultado)
    else:
        resultado = num1+num2
        print (num1, "+", num2, "=", resultado)

elif operacao == '2':
    resultado = num1*num2
    print (num1, "*", num2, "=", resultado)

elif operacao == '3':
    if num2 == 0:
        print ('nao existe divisao por ZERO')
    else:
        resultado = num1/num2
        print (num1, "/", num2, "=", resultado)

else: 
    print('Opção inválida')


