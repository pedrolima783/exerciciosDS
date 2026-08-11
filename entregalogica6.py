quantidade = int(input("Digite a quantidade de notas que serão inseridas: "))
notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota) 
soma_total = 0
for nota in notas:
    soma_total += nota  
media = soma_total / quantidade
print("-" * 30)
print(f"Média da turma: {media:.2f}")
if media >= 7.0:
    print("Classificação: Desempenho Satisfatório")
else:
    print("Classificação: Desempenho Insatisfatório")
print("-" * 30)