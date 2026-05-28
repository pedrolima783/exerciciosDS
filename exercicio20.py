n1=float(input("Digite o 1º numero: "))
n2=float(input("Digite o 2 numero: ")) 
n3=float(input("Digite o 3º numero: "))
numeros=[n1,n2,n3]
crescente=sorted(numeros)
decrescente=sorted(numeros, reverse=True)
print(f"Ordem crescente: {crescente}")
print(f"Ordem decrescente: {decrescente}")