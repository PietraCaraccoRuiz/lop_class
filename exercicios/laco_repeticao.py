"""

#lista int

frutas = ['maca', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

print("\n")

for fruta in frutas:
        print(fruta)
print("\n Primeiro elemento")
print(frutas[0])


#String

mensagem = "hello world!"

for cractere in mensagem:
    print(cractere)

#tupla
cores = ("vermelho", "verde", "azul", "amarelo")
for cor in cores:
    print("Cor:", cor)

# dicionario

pessoa = {
    #pares:
    # "chave" : "valor"
    "nome" : "ana",
    "idade" : 30,
    "profissão" : "engenharia"
}

print(pessoa["nome"])
for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")

# if no for

pessoa = {
    #pares:
    # "chave" : "valor"
    "nome" : "ana",
    "idade" : 30,
    "profissão" : "engenharia"
}

print(pessoa["nome"])
for chave, valor in pessoa.items():
    if chave == "nome":
        print(f"{chave} : {valor}")

# teste

pessoa = {
    #pares:
    # "chave" : "valor"
    "nome" : "ana",
    "idade" : 30,
    "profissão" : "engenharia"
}

print(pessoa["nome"])
for chave, valor in pessoa.items():
    if chave == "nome":
        print(f"{chave} : {valor}")
    print("acabou o if")
print("acabou o for")

# dicionario dentro de dicionario
alunos = {
    "123" : {
        "nome" : "Lucas",
        "idade" : 17
    },
    "456" : {
        "nome" : "Maria",
        "idade" : 18
    }
}

for ra, dados in alunos.items():
    print(f"RA: {ra}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()} : {valor}")

# acessando nome da aluna
print(alunos["456"]["nome"])

# conjunto = ordem aleatotia

animais = {"gato", "cachorro", "elefante", "girafa"}
for animal in animais:
    print("Animal: ", animal)

#range
for numero in range(5):
    print(numero)

print("\n")
for numero in range(1,5):
    print(numero)

print("\n")
for numero in range(0, 11, 2):
    print(numero)

print("\n")
for numero in range(0, 11, 3):
    print(numero)

"""

nome_arquivo = "arquivo.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())