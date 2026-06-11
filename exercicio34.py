def media(lista):
    return sum(lista) / len(lista)

notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]

print("\nNotas digitadas:")
print(*notas)

print(f"Média = {media(notas):.2f}")