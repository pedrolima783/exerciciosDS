def energia_cinetica():
    m = float(input("Digite a massa (kg): "))
    v = float(input("Digite a velocidade (m/s): "))
    ec = (m * v**2) / 2
    print("Energia Cinética =", ec, "J")

energia_cinetica()