
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

#O aumento no salário
valor1 = int(input())
valor2 = int(input()) 

resposta = (valor1 * valor2) / 100

print(resposta)

#O salário reajustado
valor1 = int(input())
valor2 = float(input()) 

resposta1 = (valor1) * (valor2 / 100)
resposta2 = resposta1 + valor1

print(resposta2)

#Minuteria
valor1 = int(input())
valor2 = int(input()) 

resposta1 = valor1 * 60
resposta2 = resposta1 + valor2

print(resposta2)

#Horas e minutos
valor1 = int(input())
 

resposta1 = valor1 // 60
resposta2 = valor1 % 60

print(valor1, "min = ", resposta1, "h", resposta2, "min", sep="")

#Proporções
valorEx1 = int(input())
valorEx2 = int(input())
valorEx3 = int(input())
valorEx4 = int(input())

valorRe1 = int(input())
valorRe2 = int(input())
valorRe3 = int(input())
valorRe4 = int(input())

resultado1 = (100 * valorRe1) / valorEx1
resultado2 = (100 * valorRe2) / valorEx2
resultado3 = (100 * valorRe3) / valorEx3
resultado4 = (100 * valorRe4) / valorEx4

print('%.1f' % resultado1)
print('%.1f' % resultado2)
print('%.1f' % resultado3)
print('%.1f' % resultado4)

#Problemas com juros compostos
valor1 = float(input())
valor2 = float(input())

resposta1 = valor1 * (valor2 + 1) **1
resposta2 = valor1 * (valor2 + 1) **2
resposta3 = valor1 * (valor2 + 1) **3 

print('%.2f' % resposta1)
print('%.2f' % resposta2)
print('%.2f' % resposta3)

#porcentagem 1
valor1 = float(input())
valor2 = int(input())

resposta1 = valor1 * (valor2 / 100)

print('%.2f' % resposta1)

#leolinda
valor1 = int(input())
valor2 = int(input())

resposta = valor2 - valor1

print(resposta)