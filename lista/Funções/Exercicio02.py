def maior_n(n, maior):
    if n > maior:
        maior = n
    return maior

continuar = True
maior = 0

while continuar:
    numero = int(input("Digite um numero: "))

    maior = maior_n(numero, maior)

    opcao = int(input("Deseja continuar?  1- SIM  2-NÃO"))
    if opcao == 1:
        continuar = True
    else:
        continuar = False

print("\nO maior numero é: ", maior)