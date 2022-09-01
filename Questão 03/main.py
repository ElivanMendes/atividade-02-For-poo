quantity = int(input('Informe Quantos Numeros Deseja Inserir: '))

highest_value = ''
count = ''

for x in range(0, quantity):
    number = int(input(f'Informe o {x + 1} Numero: '))

    if x != 0:
        if number == highest_value:
            count += 1
        elif number > highest_value:
            highest_value = number
            count = 1
    else:
        highest_value = number
        count = 1

print(f'\nMaior Valor: {highest_value}\nQuantidade de Vezes: {count}')
