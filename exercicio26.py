numero = int(input("Digite um número: "))

print(f"\n=== TABUADA DO {numero} ===\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")