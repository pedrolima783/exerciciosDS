numero = int(input("Digite até qual número contar: "))
forma = input("Digite 'c' para crescente ou 'd' para decrescente: ")

if forma == 'c':
    i = 1
    while i <= numero:
        print(i)
        i += 1

elif forma == 'd':
    i = numero
    while i >= 1:
        print(i)
        i -= 1

else:
    print("Forma inválida!")