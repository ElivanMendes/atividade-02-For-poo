number = int(input('Informe um Numero Positivo e Inteiro: '))

previus = 0
next = 1
sum = 1

for x in range(0, number):
    print(f'{previus} ', end='')
    sum = previus + next
    previus = next
    next = sum
