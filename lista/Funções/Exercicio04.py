def calcular_troco(compra, pago):
    if pago < compra:
        print("Pagamento insufiente")
        return 0
    else:
        troco = pago - compra
        return troco

compra = float(input("Digite valor da compra: "))
pago = float(input("Digite valor pago: "))

troco = calcular_troco(compra, pago)
print(f"O troco a ser pago é R${troco:.2f}")