matriz = [
    [
        int(input(f"[{l}][{c}] = "))
        for c in range(2)
    ]
    for l in range(2)
]

soma = sum(valor[i] for i, valor in enumerate(matriz))

print("\nSoma da diagonal =", soma)