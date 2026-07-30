def lei_ohm():
    u = float(input("Digite a tensão (V): "))
    r = float(input("Digite a resistência (Ω): "))
    i = u / r
    print("Corrente =", i, "A")

lei_ohm()