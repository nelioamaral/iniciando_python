enunciado = print('Para converter a temperatura em graus Farenheit, digite abaixo o valor em ºC')
temperatura = float(input('Digite o valor em ºC: '))
print(f'O valor de {temperatura:.2f} ºC, equivale a {1.8*temperatura+32:.2f}ºFarenheit\ntambém equivale a {temperatura+273}ºKelvin')
