#1.	Calcule a soma de 2 números.

'''
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

print("A soma é", numero2 + numero1)
'''


# 2.	Verifique se o número é ímpar

'''
numero =  int(input("Digite um número: "))

print("Número", numero ,"é impar: ", numero % 2 != 0)
'''


#3.	Verifique se pelo menos uma das condições é verdadeira, se valor1  é maior que 3 ou se valor 2 é menor que 4.

'''
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

print(valor1 ," é maior que 3: ", valor1 > 3)
print(valor2 ," é menor que 4: ", valor1 < 4)
'''


#4.	Calcule o valor absoluto.

'''
numero = int(input("Digite um valor: "))

print((numero ** 2) ** 0.5)
'''

#5.	Verifique se ambos os valores são pares.

'''
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

print(numero1 ,"e", numero2 ," são pares: ", numero1 % 2 == 0 and numero2 % 2 == 0)
'''



#6.	Verifique se pelo menos um dos valores é negativo

'''
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

print("Um dos valores é negativo: ", numero1 < 0 or numero2 < 0)
'''

#7.	Calcule a média de 3 valores.

'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print("A média é : ", (nota1 + nota2 + nota3)/3)
'''

#8.	Imprima se o resultado da expressão abaixo é True ou False: valor1 + 15 é igual a valor2 * 3

'''
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

print("valor1 + 15 é igual a valor2 * 3: ", valor1 + 15 == valor2 * 3)
'''

#9.	Calcule o resultado e o resto da divisão entre o dividendo e o divisor. Exiba todas as informações.

'''
dividendo = int(input("Digite o valor do dividendo: "))
divisor = int(input("Digite o valor do divisor: "))

print("O resultado da divisão é: ", dividendo/ divisor)
print("O resto da divisão é: ", dividendo % divisor)
'''

#10.	Escreva um programa que converta uma temperatura digitada de graus Celsius para Fahrenheit.

'''
c = float(input("Difite a temperatura em Celsius: "))

print(f"A temperatura em {c}°C é {(c * 1.8) + 35:.2f} °F")
'''

#11.	Escreva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O usuário deve informar seu peso em kg e altura em metros. A resposta deve ter no máximo 2 dígitos decimais.

'''
peso = float(input("Digite o seu peso(kg): "))
altura = float(input("Digite o sua altura(m): "))

print(f"O IMC é : {peso / (altura**2):.2f}")
'''

#12.	Crie um programa que calcule a média ponderada de três notas, sendo que as notas têm pesos diferentes.

'''
nota1 = float(input("Digite o 1 numero: "))
nota2 = float(input("Digite o 2 numero: "))
nota3 = float(input("Digite o 3 numero: "))
peso1 = float(input("\nDigite o 1 peso: "))
peso2 = float(input("Digite o 2 peso: "))
peso3 = float(input("Digite o 3 peso: "))

mediaari = ((nota1 *peso1) + (nota2 *peso2) + (nota3*peso3)) / 10

print(f"A média é: {mediaari}")
'''

#13.	Escreva um programa que calcule a potência de um número inteiro elevado a um expoente.

'''
numero = int(input("Digite um umero inteiro: "))
expoente = float(input("Digite o expoente: "))

print(numero, "^", expoente, " = ", numero**expoente)
'''

# DESAFIO (Obrigatório):

# 1.  	Calcule a raiz cúbica de um número.

'''
numero = float(input("Digite um número: "))

print(f"{numero}³ = {numero**(1/3):.2f}")
'''



#2.  	Crie um programa que calcule o montante final após um período de tempo com juros compostos.
# O usuário deve informar o capital, taxa de juros e tempo em anos.

'''
capital = float(input("Digite o capital (R$): "))
tj = float(input("Digite a taxa de juros (%): "))
tempo = float(input("Digite o tempo (meses): "))

print(f"O montante final é: {capital * (1 +(tj/100)) ** (tempo * 12)}")
'''