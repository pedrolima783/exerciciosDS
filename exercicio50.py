import math

def trabalho():
    f = float(input("Digite a força (N): "))
    d = float(input("Digite o deslocamento (m): "))
    angulo = float(input("Digite o ângulo (graus): "))

    t = f * d * math.cos(math.radians(angulo))
    print("Trabalho =", t, "J")

trabalho()