maior = 0

def maior_n(n):
    global maior
    if n > maior:
        maior = n
    return maior

continuar = True

while continuar:
    numero = int(input("Digite um numero: "))

    maior_n(numero)

    opcao = int(input("Deseja continuar?  1- SIM  2-NÃO"))
    if opcao == 1:
        continuar = True
    else:
        continuar = False

print("\nO maior numero é: ", maior)