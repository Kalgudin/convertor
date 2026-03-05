import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
rub = {'RUB': {'Value': 1, 'name': 'Российский рубль'}}
data['Valute'].update(rub)


class Currency:
    def __init__(self, data, name):
        self.name = name
        self.data = data['Valute'][name]

    def convector(self, curr_2, sum):
        res = round((sum * self.data['Value'] / curr_2.data['Value']), 2)
        print(f'За {sum} {self.name} вы получите {res} {curr_2.name}')
