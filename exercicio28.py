nome = input("Digite o nome: ")

while len(nome) <= 3:
    nome = input("Nome inválido. Digite novamente: ")

idade = int(input("Digite a idade: "))

while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite novamente: "))

salario = float(input("Digite o salário: "))

while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente: "))

sexo = input("Digite o sexo (f/m): ").lower()

while sexo != "f" and sexo != "m":
    sexo = input("Sexo inválido. Digite novamente (f/m): ").lower()

estado = input("Estado civil (s,c,v,d): ").lower()

while estado not in ["s", "c", "v", "d"]:
    estado = input("Estado inválido. Digite novamente: ").lower()

print("Dados válidos!")