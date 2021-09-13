c = int(input('Informe a quantidade de cigarros fumados em um dia: '))
a = int(input('Informe há quantos anos você é fumante: '))
perda = (a*365)*(c*10)
dias = perda/1440
print(f'O total de dias de vida perdidos é de {dias: .1f}')
