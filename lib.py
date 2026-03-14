import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
rub = {'RUB': {'Value': 1, 'name': 'Российский рубль'}}
data['Valute'].update(rub)


class Currency:
    def __init__(self, data, name):
        self.name = name.upper()
        self.data = data['Valute'][name.upper()]
        self.res = 0

    def convector(self, curr_2, sum):
        self.res = round((sum * self.data['Value'] / curr_2.data['Value']), 2)
        return f'За {sum} {self.name} вы получите {self.res} {curr_2.name}'

# Проверка связи 
