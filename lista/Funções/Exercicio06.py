def contar_vogais(palavra):
    vogais = 0
    for i in palavra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vogais+= 1
    return vogais

palavra = input("Digite uma palavra: ")
print("quantidade voagais: ", contar_vogais(palavra))