import sty
from sty import fg, bg, ef, rs

ilustracaoLOne = '------------------------------'
ilustracaoLTwo = '******************************'
ilustracaoLTree = 'CALCULADORA CLI'

print(ilustracaoLOne.center(50))
print(ilustracaoLTwo.center(50))
print(ilustracaoLTree.center(50))
print(ilustracaoLTwo.center(50))
print(ilustracaoLOne.center(50))

while True:
  optionIlustracao = '''
  [1] - Soma
  [2] - Subtração
  [3] - Multiplicação
  [4] - Divisão
  [5] - Exponeciação
  [0] - Sair
  '''
  print(optionIlustracao)
  
  optionSelect = int(input('Escolha uma opção: '))
  
  def inputNumber():
    numOne = float(input('\nDigite um número: '))
    numTwo = float(input('Digite outro número: '))
    return numOne, numTwo;
  
  def sum(numOne, numTwo):
    soma = numOne + numTwo
    print(ef.bold + f'O resultado da operação é: {soma}' + rs.all)
  
  def sub(numOne, numTwo):
    subtracao = numOne - numTwo
    print(ef.bold + f'O resultado da operação é: {subtracao}' + rs.all )
  
  def mult(numOne, numTwo):
    multiplicacao = numOne * numTwo
    print(ef.bold + f'O resultado da operação é: {multiplicacao}' + rs.all)
  
  def divi(numOne, numTwo):
    divisao = numOne / numTwo
    print(ef.bold + f'O resultado da operação é: {divisao}' + rs.all)
  
  def expo(numOne, numTwo):
    exponeciacao = numOne ** numTwo
    print(ef.bold + f'O resultado da operação é: {exponeciacao}' + rs.all)
  
  
  match optionSelect:
    case 1:
      numOne, numTwo = inputNumber()
      sum(numOne, numTwo)
    case 2:
      numOne, numTwo = inputNumber()
      sub(numOne, numTwo)
    case 3:
      numOne, numTwo = inputNumber()
      mult(numOne, numTwo)
    case 4:
      numOne, numTwo = inputNumber()
      if(numTwo == 0):
        print(fg.red + ef.bold + 'Impossível dividir por 0' + rs.all)
      else:
        divi(numOne, numTwo)
    case 5:
      numOne, numTwo = inputNumber()
      expo(numOne, numTwo)
    case 0:
      print('Saindo...')
      break;
print('Programa Encerrado')