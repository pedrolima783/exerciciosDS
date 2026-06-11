def calcular_muv(s0, v0, t, a):
    s = s0 + v0 * t + (1/2) * a * (t ** 2)
    return s


print("=" * 40)
print(" CALCULADORA DE MOVIMENTO UNIFORMEMENTE VARIADO ")
print("=" * 40)

print("\nEquação da posição:")
print("S = S0 + V0 × t + 1/2 × a × t²\n")

s0 = float(input("Digite a posição inicial (S0) em metros: "))
v0 = float(input("Digite a velocidade inicial (V0) em m/s: "))
t = float(input("Digite o tempo (t) em segundos: "))
a = float(input("Digite a aceleração (a) em m/s²: "))

resultado = calcular_muv(s0, v0, t, a)

print("\n===== RESULTADO =====")
print(f"S = {s0} + ({v0} × {t}) + 1/2 × {a} × {t}²")
print(f"Posição final (S) = {resultado:.2f} metros")

print("\n===== ANÁLISE =====")
if a > 0:
    print("O movimento está acelerando.")
elif a < 0:
    print("O movimento está desacelerando.")
else:
    print("O movimento possui velocidade constante.")

print("\nPrograma finalizado!")