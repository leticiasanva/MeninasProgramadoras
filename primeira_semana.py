
#nomes alternativos #1
primeiro_nome = input()
nome_do_meio = input()
sobrenome = input()

print(primeiro_nome)
print(sobrenome)
print(primeiro_nome, sobrenome)
print(primeiro_nome, nome_do_meio, sobrenome)

#nomes alternativos #2
primeiro_nome = input()
nome_do_meio = input()
sobrenome = input()

print(primeiro_nome + ' ' + nome_do_meio + ' ' + sobrenome) 
print(primeiro_nome + ' ' + sobrenome)
print(sobrenome + ', ' + primeiro_nome)

#Brincando com sequências de caracteres
valor1 = input()
valor2 = input()
valor3 = input()
valor4 = input()
valor5 = input()

resposta1 = valor1 + valor3
resposta2 = valor2 + valor4
resposta3 = (resposta1 + resposta2) * int(valor5)

print(resposta1)
print(resposta2)
print(resposta3)

#the next
valor = int(input())

print(valor + 1)

#o anterior
valor = int(input())

print(valor - 1)

#o dobro
valor = int(input())

print(valor * 2)

#decimais à moda antiga
valor = float(input())

print('%.2f' % valor)
print('%.4f' % valor)
print('%.6f' % valor)
print('%.8f' % valor)
print('%.10f' % valor)

#a metade
valor = int(input())

resposta1 = valor / 2

print('%.1f' % resposta1)

#A Divisão Inteira
valor1 = int(input())
valor2 = int(input())

resposta1 = valor1 // valor2
resposta2 = valor1 % valor2

print(resposta1)
print(resposta2)

#Soma, subtração, multiplicação, divisão, módulo, divisão inteira e potência
valor1 = int(input())
valor2 = int(input())

resposta1 = valor1 + valor2
resposta2 = valor1 - valor2
resposta3 = valor1 * valor2
resposta4 = '%.2f' % (valor1 / valor2)
resposta5 = valor1 % valor2
resposta6 = valor1 // valor2
resposta7 = valor1 ** valor2

print(resposta1)
print(resposta2)
print(resposta3)
print(resposta4)
print(resposta5)
print(resposta6)
print(resposta7)

#PIN perigoso
valor1 = int(input())
valor2 = int(input())

resposta1 = valor1 + valor2

print(resposta1)

#A Compra Questionável
valor1 = int(input())
valor2 = int(input())

resposta = valor1 - valor2

print(resposta)