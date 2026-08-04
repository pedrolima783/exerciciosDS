quantidade_notas = int(input("Digite a quantidade de notas que serão inseridas: "))

lista_notas = []

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    lista_notas.append(nota)

soma_notas = 0.0
for nota in lista_notas:
    soma_notas += nota
media_turma = soma_notas / quantidade_notas
print(f"\nA média da turma é: {media_turma:.2f}")
if media_turma >= 7.0:
    print("Classificação: Desempenho Satisfatório")
else:
    print("Classificação: Desempenho Insatisfatório")
