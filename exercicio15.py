peso=float(input("Digite o peso evdo peixe em kg:"))
limite=50
multa_por_kg=4.00
if peso>limite:
    excesso=peso-limite
    multa=excesso*multa_por_kg
    print(f'Excesso: {excesso:.2f} kg')
    print(f"multa a pagar: R$ {multa:.2f}")
else:
    excesso=0
    multa=0
    print("Excesso: 0.00 kg")
    print("Multa a pagar: R$0.00")
