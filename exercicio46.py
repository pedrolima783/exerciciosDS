def queda_livre():
    t = float(input("Digite o tempo (s): "))
    g = 9.8
    h = (g * t**2) / 2
    print("Altura =", h, "m")

queda_livre()