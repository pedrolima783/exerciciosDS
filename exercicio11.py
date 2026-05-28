altura=float(input("digite a altura em metros: "))
sexo=input("digite o sexo [M/F]: ").upper()
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para homem: {peso_ideal:.2f} kg")
elif sexo == 'F':
    peso_ideal=(62.1 * altura) - 44.7
    print(f"Peso ideal para mulher: {peso_ideal:.2f} kg")
else:
    print("sexo invalido. Digite M para masculino ou F para feminino.")