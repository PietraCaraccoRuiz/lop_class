def contagem_regressiva(n):
    if n > 0:
        print(n)
        contagem_regressiva(n -1)
    return "Fim"

n = int(input("Digite um número inteiro: "))
print(contagem_regressiva(n))