vendas = [# Vendedor 0 (Mês 0, Mês 1, Mês 2),  # Vendedor 1 (Mês 0, Mês 1, Mês 2)
[900, 1700, 1600]]
print("--- Vendas por Vendedor ---")
for i in range(len(vendas)):
    print(f"Vendedor {i}: {vendas[i]}")
print("\n--- Totais por Vendedor ---")
totais_vendedores = []
for i in range(len(vendas)):
    soma_vendedor = 0
    for j in range(len(vendas[i])):
        soma_vendedor += vendas[i][j]
    totais_vendedores.append(soma_vendedor)
    print(f"Total vendedor {i}: R$ {soma_vendedor}")
print("\n--- Totais por Mês ---")
qtd_linhas = len(vendas)
qtd_colunas = len(vendas[0])
for j in range(qtd_colunas):
    soma_mes = 0
    for i in range(qtd_linhas):
        soma_mes += vendas[i][j]
    print(f"Total mês {j}: R$ {soma_mes}")
print("\n--- Total Geral ---")
total_geral = 0
for i in range(len(vendas)):
    for j in range(len(vendas[i])):
        total_geral += vendas[i][j]
print(f"Total geral da empresa: R$ {total_geral}")
maior_venda = -1
melhor_vendedor = -1

for i in range(len(totais_vendedores)):
    if totais_vendedores[i] > maior_venda:
        maior_venda = totais_vendedores[i]
        melhor_vendedor = i
print(f"O melhor vendedor é o Vendedor {melhor_vendedor} (Total: R$ {maior_venda})")