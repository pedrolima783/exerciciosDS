alunos = []

for aluno in range(10):

    notas = [
        float(input(f"Aluno {aluno+1} - Nota {n+1}: "))
        for n in range(4)
    ]

    alunos.append(sum(notas) / 4)

aprovados = sum(media >= 7 for media in alunos)

print(f"\nQuantidade de aprovados: {aprovados}")