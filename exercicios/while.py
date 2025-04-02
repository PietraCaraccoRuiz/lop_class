# exemplo while

num = 1
while num <= 10:
    print(num)
    num = num + 1

# contagem regressiva

start = int(input("Digite um número de 5 a 10: "))

while start !=0:
    print(start)
    start -= 1

# maior numero

i =1
maior = 0
while i<= 5:
    numero = int(input("digite um numero: "))
    if numero > maior:
        maior = numero
    i += 1

print("Maior numero é", maior)

# fatorial
numero = int(input("Digite um numero: "))

fat = numero
while numero >= 2:
    fat = fat * (numero-1)
    numero -= 1
print("O resultado é: ", fat)

# metas
lista = []

opcao = 1
i= 0
soma = 0

while opcao!= 0:
    numero = int(input("Digite a nota: "))
    lista.insert(i,numero)
    soma += lista[i]
    i += 1
    opcao = int(input("\nDeseja continuar:\n1- SIM \n0- Não"))

media = soma/ i
print(soma)
print(media)
print(lista)


# calculadora
print("1- somar")
print("2- subtrair")
print("3- multiplicar")
print("4- dividir")
print("5- sair")
opcao = int(input("Digite a escolha: "))

res = 0
numero1 = float(input("\ndigite um numero: "))
numero2 = float(input("\ndigite outro numero: "))

while opcao != 5:
    if opcao == 1:
        res = numero1 + numero2
    elif opcao == 2:
        res = numero1 - numero2
    elif opcao == 3:
        res = numero1 ** numero2
    elif opcao == 4:
        res = numero1 / numero2
    else:
        print("opcão inválida!")
    print("O resultado da operação é: ", res)
    opcao = int(input("Digite a escolha: "))


