def potencia_eletrica():
    e = float(input("Digite a energia (J): "))
    t = float(input("Digite o tempo (s): "))
    p = e / t
    print("Potência =", p, "W")

potencia_eletrica()