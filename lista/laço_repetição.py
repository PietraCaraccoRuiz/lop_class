import random

opcao = int(input("Escolha o exercicio: "))

# 1) Peça 10 números e conte quantos são múltiplos de 3. Use for.
if opcao == 1:
    mult = 0
    i = 0
    for i in range(10):
        numero = int(input("\nDigite um número: "))
        if numero % 3 == 0:
            mult += 1
    print("São multiplos de 3: ", mult, " numeros")


# 2) Crie um programa que simule o uso de senha com tentativas infinitas
# até digitar a senha correta (use while True).
elif opcao == 2:
    while True:
        tentativa = input("\nDigite um número: ")
        senha = "123"
        if  tentativa == senha:
            print("Acertou!!")
            break
        else:
            print("errou tente denovo!")

elif opcao == 3:
    # MENU

    while opcao != "Sair":
        print(" - Continuar")
        print(" - Sair")
        opcao = input()

#    4) Crie um programa que peça dois números
#    inteiros e exiba todos os números entre eles que são primos. Use for.
elif opcao == 4:

    numero1 = int(input("digite um numero: "))
    numero2 = int(input("digite outro numero: "))
    j = 0

    for i in range(numero1, numero2+ 1):
        cont = 0
        for j in range(1,numero2 + 1):
            if i % j == 0:
                cont += 1
        if cont == 2:
            print("número primo: ", i)

elif opcao == 5:
    tentativa = 3
    senha = "123"
    while tentativa != 0:
        senha_tentativa = input("Digite a senha: ")
        if senha_tentativa == senha:
            print("Você acertou!!")
            tentativa = 0
        else:
            print("Você errou!!\n voce tem ", tentativa, " tentativas")
            tentativa -= 1

elif opcao == 6:
    i = 1
    par = []
    impar = []
    for i in range(1, 11):
        numero = int(input(f"Digite o {i}° número: "))
        if numero % 2 == 0:
            par.insert(0, numero)
        if numero % 2 != 0:
            impar.insert(0, numero)
    print(f"Números pares:{par}\nNúmeros ímpares:{impar}")

elif opcao == 7:
    a = 0
    e = 0
    ii = 0
    o = 0
    u = 0

    frase = input("digite uma frase: ")
    fraseformatada = str.lower(frase)
    for i in fraseformatada:
        if i == "a":
            a += 1
        elif i == "e":
            e += 1
        elif i == "i":
            ii += 1
        elif i == "o":
            o += 1
        elif i == "u":
            u += 1
    print("Quantidade de vogais", a + e + ii + o + u)
    print("A: ", a, "\nE: ", e, "\nI: ", ii, "\nO: ", o, "\nU: ", u )

elif opcao == 8:
    cara = 0
    lista = ["cara", "coroa"]

    while cara < 3:
        moeda = random.choice(["cara", "coroa"])
        print(moeda)
        if moeda == "cara":
            cara += 1


elif opcao == 9:
    soma = 0
    quant_menores = 0
    quantidade = int(input("Digite a quantidade de números: "))
    lista = []
    for i in range(quantidade):
        numero = int(input("Digite um número: "))
        lista.insert(0,numero)
        soma += numero
    media = soma / quantidade
    print("Media: ", media)
    for item in lista:
        if item < media:
            print(item)
            quant_menores += 1
    print("Quantidade de números menores que a média: ", quant_menores)

elif opcao == 10:
    maior = 0
    aux = 100
    seg_maior = 0
    quantidade = int(input("Digite a quantidade de números: "))
    lista = []

    for i in range(quantidade):
        numero = int(input("Digite um numero: "))
        lista.insert(0, numero)

        if numero > maior:
            maior = numero

    for item in lista:
        sub = maior - item
        if sub < aux and sub !=0 :
            aux = sub
            seg_maior = item

    print("Segundo maior número: ", seg_maior)

elif opcao == 12:

    # Crie um programa que simule o crescimento de uma população de coelhos ao longo de várias gerações.
    # Os coelhos se reproduzem a uma taxa fixa a cada geração, e uma porcentagem deles morre a cada geração.
    # O programa deve solicitar ao usuário a taxa de reprodução, a taxa de mortalidade e o número inicial de coelhos.
    # Use um loop for ou while para simular várias gerações e exiba a população de coelhos após um número de gerações especificado pelo usuário.

    populacao = int(input("Digite a população: "))
    taxa_reproducao = float(input("Taxa de reprodução (%): "))
    taxa_mortalidade = float(input("Taxa de mortalidade (%): "))
    numero_geracoes = int(input("Número de gerações: "))

    for i in range(1, numero_geracoes + 1):
        nascimentos = populacao + (taxa_reproducao / 100)
        mortes = populacao + (taxa_mortalidade / 100)
        populacao = populacao + nascimentos - mortes
        print(f"{i}° geração: {populacao:.2f} ")

elif opcao == 13:
    palavras = ["estrela", "coelho", "abacaxi", "borracha", "Brasil"]
    tentativas = 6
    palavra_lista = []
    lista = []

    palavra = random.choice(palavras)

    for letra in palavra:
        print("_" , end=" ")
        palavra_lista.insert(0, letra)

    print(palavra_lista)
    while tentativas > 0:
        letra_tentativa = input("\nDigite uma letra: ")
        lista.insert(0, letra_tentativa)
        print(lista)
        for i in palavra_lista:
            if i == letra_tentativa:
                lista.insert(0,i)

        for letra in palavra:
            if palavra_lista:
                print(letra, end=" ")
