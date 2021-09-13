d = int(input('Informe a quantidade de dias: '))
h = int(input('Informe as horas: '))
m = int(input('Informe os minutos: '))
s = int(input('Informe os segundos: '))
total = (d*86400) + (h*3600) + (m*60) + s
print(f'O total em segundos é {total}')
