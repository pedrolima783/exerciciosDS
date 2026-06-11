numeros = [int(input(f"Número {i+1}: ")) for i in range(20)]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2]

print("\nTodos :", numeros)
print("Pares :", pares)
print("Ímpares:", impares)