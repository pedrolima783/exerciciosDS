#Lista
frutas = ['maçã', 'banana', 'uva']

frutas.append('laranja')
frutas.insert(1,'Pera')
frutas.remove('banana')
frutas.pop()

print('lista:', frutas)

#Matriz
matriz = [
    [10, 20],
    [30, 40]
]

matriz.append([50 ,60])
matriz.insert(1, [15, 25])
matriz.pop()

print("Matriz: ")
for linha in matriz:
    print(linha)