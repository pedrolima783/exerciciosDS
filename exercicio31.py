numeros = []

for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

maior = max(numeros)
soma = sum(numeros)
media = soma / 5

print("Maior número:", maior)
print("Soma:", soma)
print("Média:", media)