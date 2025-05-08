def eh_primo(n):
    eh_primo = 0
    for i in range(1, n+1):
        res = n % i
        if res == 0:
            eh_primo += 1
    if eh_primo == 2:
        return True
    else:
        return False

n = int(input("Digite um número: "))
print(eh_primo(n))