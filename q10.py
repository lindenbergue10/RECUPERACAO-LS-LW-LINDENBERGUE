mediaCusto = 0
mediaVenda = 0
for x in range(0,45):
    custo = int(input('Insira o custo: '))
    venda = int(input('Insira o valor de Venda: '))
    if custo>venda:
        print('Prejuízo')
    elif venda>custo:
        print('lucro')
    elif venda==custo:
        print('empate')
    mediaCusto += custo
    mediaVenda += venda
print('A média de custo é: %d'%(mediaCusto/45))
print('A média de venda é: %d'%(mediaVenda/45))
