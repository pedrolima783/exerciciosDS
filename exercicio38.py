def criar_matriz(linhas, colunas):

    return [
        [
            int(input(f"[{l}][{c}] = "))
            for c in range(colunas)
        ]
        for l in range(linhas)
    ]

matriz = criar_matriz(3, 3)

print()

for linha in matriz:
    print(*linha)