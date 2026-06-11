def velocidade_media(delta_s, delta_t):
    v = delta_s / delta_t
    return v

distancia = float(input("Digite a variação do espaço (m): "))
tempo = float(input("Digite a variação do tempo (s): "))

resultado = velocidade_media(distancia, tempo)

print("A velocidade média é:", resultado, "m/s")