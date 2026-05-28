peso=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura em metros: "))
imc=peso/(altura**2)
print(f"Seu IMC é: {imc:.1f}")
if imc<18.5:
    print("Classificação: Magreza")
elif imc<=24.9:
    print("Classificação: Normal")
elif imc<=29.9:
    print("Classificação: Sobrepeso")
elif imc<=34.9:
    print("Classificação: Obesidade grau 1")
elif imc<=39.9:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3")