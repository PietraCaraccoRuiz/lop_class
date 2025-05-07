def converter_celsius_fahrenheit(c):
    f = (c * 1.8) + 32
    return f

c = float(input("Digite a temperatura em celsius: "))
print(f"{c:.2f}C° -> {converter_celsius_fahrenheit(c):.2f}F°")
