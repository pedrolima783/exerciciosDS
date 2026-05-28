while True:
    pop_a = int(input("População A: "))
    taxa_a = float(input("Taxa de crescimento A (%): "))

    pop_b = int(input("População B: "))
    taxa_b = float(input("Taxa de crescimento B (%): "))

    anos = 0

    while pop_a < pop_b:
        pop_a += pop_a * (taxa_a / 100)
        pop_b += pop_b * (taxa_b / 100)
        anos += 1

    print("Quantidade de anos:", anos)

    repetir = input("Deseja repetir? (s/n): ").lower()

    if repetir != "s":
        break