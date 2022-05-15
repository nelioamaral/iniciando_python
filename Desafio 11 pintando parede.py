enunciado=input('Para saber quantos litros de tinta é necessário pra pintar sua parede, digite os dados abaixo. (aperte enter)')
altura=float(input('Qual é a altura da parede em metros? : '))
largura=float(input('Qual é a largura da parede em metros? : '))
print(f'Sua parede tem {altura*largura:.2f}m², será necessário {(altura*largura)/2:.2f} litros de tinta para pinta-la')
