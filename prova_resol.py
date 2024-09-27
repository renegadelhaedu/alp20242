#q2
preco_calcinha = 30
preco_sutia = 60
preco_saia = 70
preco_vestido = 90

qtde_calcinha = int(input("Digite a quantidade de calcinhas "))
qtde_sutia = int(input("Digite a quantidade de sutiãs "))
qtde_saia = int(input("Digite a quantidade de saias "))
qtde_vestido = int(input("Digite a quantidade de vestidos "))

total_calcinha = qtde_calcinha * preco_calcinha
total_sutia = qtde_sutia * preco_sutia
total_saia = qtde_saia * preco_saia
total_vestido = qtde_vestido * preco_vestido

total = total_calcinha + total_sutia + total_saia + total_vestido
totaldesconto = 0

if qtde_calcinha > 0 and qtde_sutia > 0:
    totaldesconto += total * 0.05

if total > 400:
    totaldesconto += total * 0.1

if qtde_saia >= 4:
    saias_gratis = qtde_saia // 4
    totaldesconto += saias_gratis * preco_saia

if qtde_vestido > 0 and qtde_calcinha == 0 and qtde_sutia == 0 and qtde_saia == 0 and total > 500:
    totaldesconto += total * 0.07

if qtde_sutia > 10 or qtde_calcinha > 10:
    totaldesconto += total * 0.08

total = total - totaldesconto

print(total)