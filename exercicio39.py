matriz = [
    [
        int(input(f"[{l}][{c}] = "))
        for c in range(4)
    ]
    for l in range(4)
]

print("\nMATRIZ\n")

for linha in matriz:
    print(" | ".join(map(str, linha)))