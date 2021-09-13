km = int(input('Informe a quantidade de km percorridos: '))
d = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))
pagar = (d*60) + (0.15*km)
print(f'O total a pagar pelo aluguel do carro será de R$ {pagar: .2f}')
