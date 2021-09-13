p = float(input('Informe o preço da mercadoria: '))
d = int(input('Informe o percentual de desconto: '))
d2 = (d/100)*p
pf = p - d2
print(f'O valor do produto com desconto será de R$ {pf: .2f}')
