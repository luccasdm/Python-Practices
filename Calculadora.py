def calculadora():
    valor_1 = int(input('Insira o primeiro número: '))
    valor_2 = int(input('Insira o segundo número: '))
    operador = input('''Insira o operador que deseja usar conforme abaixo:
(+) ou (soma)
(-)  ou (subtracao)
(*) ou (multiplicacao)
(/) ou (divisao)
(**) ou (expoente)
''')
    
    if valor_2 == 0 and operador in ('/', 'divisao'):
      print('Não podemos dividir nada por zero.')
    else:
      if operador == '+' or operador == 'soma':
          print('{} + {} = '.format(valor_1, valor_2), valor_1 + valor_2)

      elif operador == '-' or operador == 'subtracao':
          print('{} - {} = '.format(valor_1, valor_2), valor_1 - valor_2)

      elif operador == '*':
          print('{} * {} = '.format(valor_1, valor_2), valor_1 * valor_2)

      elif operador == '/':
          print('{} / {} = '.format(valor_1, valor_2), valor_2 / valor_2)

      elif operador == '**':
          print('{} ** {} = '.format(valor_1, valor_2), valor_2 ** valor_2)

    novamente()

def novamente():
    calcula_novamente = input('''
Você deseja realizar outro calculo?
Digite 1 para SIM e 0 para NÃO
''')

    if calcula_novamente == '1':
        calculadora()
    elif calcula_novamente == '0':
        print('Obrigado!')
    else:
        novamente()

calculadora()