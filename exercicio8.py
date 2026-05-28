n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
n4=float(input("Digite a quarta nota: "))
media=(n1+n2+n3+n4)/4
print(f"A media do aluno é: {media:.2f}")
if media>= 7.0:
    print("Situação: Aprovado")
elif media>= 4.0:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")