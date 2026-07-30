def pressao():
    f = float(input("Digite a força (N): "))
    a = float(input("Digite a área (m²): "))
    p = f / a
    print("Pressão =", p, "Pa")

pressao()