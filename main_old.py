from lib import *

ex = True
while ex:
    print('конвератция валют')
    print('доллар - USD')
    print('евро   - EUR')
    print('юань   - CNY')
    print('рубль  - RUB')

    v1 = input('Введите какую валюту вы хотите обменять: ')
    v2 = input('Введите на какую валюту вы хотите обменять: ')
    sum = int(input('Какую сумму? '))

    val_1 = Currency(data, v1)
    val_2 = Currency(data, v2)

    print(val_1.convector(val_2, sum))

    an = input('Хотите еще?(Y/N)').upper()
    if an == 'N':
        ex = False

print("До свидания!")
