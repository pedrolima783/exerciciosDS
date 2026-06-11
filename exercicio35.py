vogais = "aeiou"

caracteres = [input("Digite uma letra: ").lower() for _ in range(10)]

consoantes = list(filter(
    lambda letra: letra.isalpha() and letra not in vogais,
    caracteres
))

print("Consoantes encontradas:")
print(*consoantes)

print("Quantidade:", len(consoantes))