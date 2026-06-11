def ler_vetor(tamanho):
    return [int(input(f"Valor {i+1}: ")) for i in range(tamanho)]

vetor = ler_vetor(5)

print("Vetor:", *vetor)