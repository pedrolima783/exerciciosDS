numeros = [float(input(f"Número {i+1}: ")) for i in range(10)]

print("Inverso:")
print(*reversed(numeros))