import random

opcao = int(input("Escolha o exercicio: "))

while opcao != 0:
    if opcao == 1:
        # Peça para o usuário digitar um ano e retorne se ele é um Ano Bissexto
        ano = int(input("Digite um ano: "))
        if ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0:
            print("A ano é bissexto")
        else:
            print("A não é bissexto")
    elif opcao == 2:
        # Calcular IMC
        peso = float(input("Qual é o peso(kg): "))
        altura = float(input("Qual é a altura(m): "))
        imc = peso / altura ** 2
        print(f"Seu IMC é: {imc:.2f}")
        if imc < 18.5:
            print("Baixo peso")
        elif 18.5 < imc < 24.9:
            print("Normal")
        elif 25 < imc < 29.9:
            print("Sobrepeso")
        elif 30 < imc < 34.9:
            print("Obesidade")
        elif 35 < imc < 39.9:
            print("Obesidade Mórbida")
        elif imc > 40:
            print("Obesidade Mórbida")
        else:
            print("Nenhum")
    elif opcao == 3:
        # Calculadora desconto de produto
        quant = int(input("Digite a quantidade: "))
        valor = float(input("Digite o valor: "))

        if quant > 100:
            desconto = 10 / 100
        else:
            desconto = 5 / 100

        res = valor - (valor * desconto)

        print("Quantidade: ", quant)
        print("Valor inicial do produto: ", valor)
        print("Valor com desconto do produto: ", res)
        print("Valor total a pagar: ", res * quant)

    elif opcao == 4:
        idade = int(input("Digite sua idade: "))

        if 18 < idade < 70:
            print("Voto Obrigatório")
        elif 16 <= idade < 18 or idade >= 70:
            print("Voto Facultativo")
        else:
            print("não Eleitor")

    elif opcao == 5:
        idade1 = int(input("idade da 1 pessoa: "))
        idade2 = int(input("idade da 2 pessoa: "))
        idade3 = int(input("idade da 3 pessoa: "))

        if idade1 > idade2 > idade3:
            print(f"Idade {idade1} é maior\nIdade {idade3} é menor")
        elif idade1 > idade3 > idade2:
            print(f"Idade {idade1} é maior\nIdade {idade2} é menor")
        elif idade2 > idade1 > idade3:
            print(f"Idade {idade2} é maior\nIdade {idade3} é menor")
        elif idade2 > idade3 > idade1:
            print(f"Idade {idade2} é maior\nIdade {idade1} é menor")
        elif idade3 > idade1 > idade2:
            print(f"Idade {idade3} é maior\nIdade {idade2} é menor")
        else:
            print(f"Idade {idade3} é maior\nIdade {idade1} é menor")
    elif opcao == 6:
        hora = int(input("Digite a hora: "))
        minutos = int(input("Digite os minutos: "))
        segundos = int(input("Digite os segungos: "))

        if 0 <= hora < 25:
            if 0 <= minutos < 61:
                if 0 <= segundos < 61:
                    print("Hora válida")
                else:
                    print("Hora inválida")
            else:
                print("Hora inválida")
        else:
            print("Hora inválida")

    elif opcao == 7:
        nota = float(input("Digite sua nota: "))
        if 0 <= nota < 3:
            nota = "E"
        elif 3 <= nota < 5:
            nota = "D"
        elif 5 <= nota < 7:
            nota = "C"
        elif 7 <= nota < 9:
            nota = "B"
        elif 9 <= nota <= 10:
            nota = "A"
        else:
            print("Nota inválida")
            break
        print("A nota é ", nota)
    elif opcao == 8:
        lado1 = float(input("Digite um lado: "))
        lado2 = float(input("Digite um lado: "))
        lado3 = float(input("Digite um lado: "))
        lado4 = float(input("Digite um lado: "))

        if lado1 == lado2 == lado3 == lado4:
            print("É quadrado")
        elif (lado1 == lado2 or lado3 == lado4) or (lado1 == lado3 or lado2 == lado4) or (
                lado2 == lado3 or lado1 == lado4):
            print("Retangulo")
        else:
            print("Nehnum dos dois")

    elif opcao == 9:
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        operacao = input("Digite a operação(+, -, *, /): ")

        if operacao == "+":
            print(f"{numero1} {operacao} {numero2} = {numero1 + numero2}")
        elif operacao == "-":
            print(f"{numero1} {operacao} {numero2} = {numero1 - numero2}")
        elif operacao == "*":
            print(f"{numero1} {operacao} {numero2} = {numero1 * numero2}")
        if operacao == "/":
            print(f"{numero1} {operacao} {numero2} = {numero1 / numero2}")
        else:
            print("Operação inválida")

    elif opcao == 10:

        media = 0
        nota1 = float(input("Digite a 1 nota: "))

        nota2 = float(input("Digite a 2 nota: "))

        nota3 = float(input("Digite a 3 nota: "))

        if nota2 > nota1 < nota3:

            media = (nota2 + nota3) / 2

        elif nota1 > nota2 < nota3:

            media = (nota1 + nota3) / 2

        elif nota2 > nota3 < nota1:

            media = (nota1 + nota2) / 2
        print("Média é: ", media)

    elif opcao == 11:
        tentativa = 2
        acertou = False
        print("========================================\n\t\tDESAFI0\n\t\tAdivinhe qual é o número de 1 a 10!")
        escolha = random.randint(1, 10)
        print("\n\t\tO número é: ?\n\t\tVoce tem", tentativa, "tentativas!")
        print("========================================\n\n")
        numero = int(input(" Qual é o número: "))

        if numero == escolha:
            print("Você acertou! Parabéns!")
            acertou = True
        elif numero > escolha:
            tentativa -= 1
            print("OPS! Você errou... Tem", tentativa, "tentativas restantes")
            print("Dica: O numero é menor")
        elif numero < escolha:
            tentativa -= 1
            print("OPS! Você errou... Tem", tentativa, "tentativas restantes")
            print("Dica: O numero é maior")

        if not acertou:
            numero = int(input("\n Tente denovo!\n Qual é o número: "))
            if numero == escolha:
                print("Você acertou! Parabéns!")
            elif numero > escolha:
                tentativa -= 1
                if tentativa == 0:
                    print("Suas tentativas acabaram....Você Perdeu!")
                    break
                print("OPS! Você errou... Tem", tentativa, "tentativas restantes")
                print("Dica: O numero é menor")
            elif numero < escolha:
                tentativa -= 1
                if tentativa == 0:
                    print("Suas tentativas acabaram....Você Perdeu!")
                    break
                print("OPS! Você errou... Tem", tentativa, "tentativas restantes")
                print("Dica: O numero é maior")

    opcao = int(input("Escolha o exercicio: "))

else:
    print("Saindo...")