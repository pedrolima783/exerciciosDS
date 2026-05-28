import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("Não é uma equação do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    print("Delta =", delta)

    if delta < 0:
        print("A equação não possui raízes reais.")

    elif delta == 0:
        x = -b / (2*a)
        print("A equação possui apenas uma raiz real:")
        print("x =", x)

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("A equação possui duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)