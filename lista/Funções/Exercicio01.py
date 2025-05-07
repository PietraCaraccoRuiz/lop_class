def calcular_imc(altura, peso):
    imc = peso / (altura ** 2)
    return imc

altura = float(input("Digite sua altura(m): "))
peso = float(input("Digite seu peso(kg): "))
print("Seu imc é: ", calcular_imc(altura, peso))