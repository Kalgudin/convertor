from tkinter import *
from tkinter import ttk
import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
rub = {'RUB': {'Value': 1, 'Name': 'Российский рубль'}}

def get_val_list(data):
    vl = ['RUB', 'USD', 'EUR', 'CNY']

    data['Valute'].update(rub)
    vl.extend(list(data['Valute'].keys()))
    return vl

def click():
    v1=data['Valute'][valut_1.get()]
    v2=data['Valute'][valut_2.get()]

    val_1 = float(v1['Value'])
    val_2 = float(v2['Value'])

    v1_name = data['Valute'][valut_1.get()]['Name']
    v2_name = data['Valute'][valut_2.get()]['Name']

    sum = float(fill_summ.get())
    res_1 = round((sum * val_1 / val_2), 2)
    res_2 = round((sum * val_2 / val_1), 2)

    left_text['text'] = f'За {sum} {v1_name}  вы получите {res_1} {v2_name}'
    right_text['text'] = f'За {sum} {v2_name}  вы получите {res_2} {v1_name}'

val_list = get_val_list(data)

root = Tk()  # создаем корневой объект - окно
root.title("Конвертор валют на Tkinter")  # устанавливаем заголовок окна
root.geometry("800x600")  # устанавливаем размеры окна


Label(text="Добро пожаловать в Конвертор валют", height=3, width=50, borderwidth=3, background='#edc2d8').pack(anchor=NW, fill=X, padx=5, pady=5)  # создаем текстовую метку
Label(text="Здесь вы можете произвести расчет кросс-курсов различных валют", height=3, width=50, borderwidth=3, background='#d7d8ea').pack(anchor=NW, fill=X, padx=5, pady=5)

frame_1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[5,20])
for c in range(3): frame_1.columnconfigure(index=c, weight=1)

Label(frame_1, text="Валюта", height=3, width=50, background='#e4edc2').grid(row=0, column=0, padx=5, pady=5)
Label(frame_1, text="Сумма", height=3, width=50, background='#e4edc2').grid(row=0, column=1, padx=5, pady=5)
Label(frame_1, text="Валюта", height=3, width=50, background='#e4edc2').grid(row=0, column=2, padx=5, pady=5)

valut_1 = ttk.Combobox(frame_1, width=30, values=val_list)
fill_summ = ttk.Entry(frame_1, width=30, background='#d9d9ea')
valut_2 = ttk.Combobox(frame_1, width=30, values=val_list)

btn = ttk.Button(root, width=120, text="Расчет", command=click)

frame_2 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[5,20])
for c in range(2): frame_2.columnconfigure(index=c, weight=1)

left_text = Label(frame_2, text="", height=3, width=50, background='#e4edc2')
right_text = Label(frame_2, text="", height=3, width=50, background='#e4edc2')

frame_1.pack(anchor=NW, fill=X, padx=5, pady=5)

valut_1.grid(row=0, column=0, padx=5, pady=5)
fill_summ.grid(row=0, column=1, padx=5, pady=5)
valut_2.grid(row=0, column=2, padx=5, pady=5)

btn.pack(anchor=NW, fill=X, padx=5, pady=5)

frame_2.pack(anchor=NW, fill=X, padx=5, pady=5)

left_text.grid(row=0, column=0, padx=5, pady=5)
right_text.grid(row=0, column=1, padx=5, pady=5)


root.mainloop()



