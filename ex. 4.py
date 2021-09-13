s = float(input('Informe o salário: '))
a = float(input('Informe a porcentagem de aumento: '))
a2 = (a/100)*s
sn = a2 + s
print(f'O aumento salarial será de R$ {a2: .2f} e o salário final será R$ {sn: .2f}')
