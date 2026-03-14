from tkinter import *
from tkinter import ttk
import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

def get_val_list():
    vl = ['USD', 'EUR', 'CNY']

    rub = {'RUB': {'Value': 1, 'name': 'Российский рубль'}}
    data['Valute'].update(rub)
    vl.extend(list(data['Valute'].keys()))
    return vl


def click():
    valut_fild['text'] = valut.get()
    result_fild['text'] = calculation(valut_fild['text'], int(fill_summ.get()))

def calculation(val, sum):
    if bay_sell.get() == 'sell':
        res = data['Valute'][val]['Value'] * int(sum)
        valut_fild['text'] = 'RUB'
    elif bay_sell.get() == 'bay':
        res = int(sum) / data['Valute'][val]['Value']
    else:
        res = "!!! WTF !!!"

    return res


val_list = get_val_list()

root = Tk()  # создаем корневой объект - окно
root.title("Обменник на Tkinter")  # устанавливаем заголовок окна
root.geometry("800x600")  # устанавливаем размеры окна

bay_sell = StringVar(value='bay')

label = Label(text="Добро пожаловать в обменник", height=3, width=50, borderwidth=3, background='#edc2d8')  # создаем текстовую метку
top_text = Label(text="Здесь вы можете узнать сумму полученную при обмене валюты", height=3, width=50, borderwidth=3, background='#d7d8ea')
bay_btn = ttk.Radiobutton(text='Покупка', value='bay', variable=bay_sell)
sell_btn = ttk.Radiobutton(text='Продажа', value='sell', variable=bay_sell)
middle_text = Label(text="Выберете валюту и сумму для обмена", height=3, width=50, borderwidth=3, background='#edd3c2')

frame_1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[5,20])
for c in range(3): frame_1.columnconfigure(index=c, weight=1)
valut = ttk.Combobox(frame_1, width=30, values=val_list)
fill_summ = ttk.Entry(frame_1, width=30, background='#d9d9ea')
btn = ttk.Button(frame_1, width=30, text="Расчет", command=click)

frame_2 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[5,3])
for c in range(3): frame_2.columnconfigure(index=c, weight=1)
bottom_text = Label(frame_2, text="Вы получите", height=3, width=30, background='#c2e8ed')
result_fild = Label(frame_2, text="", height=3, width=30, background='#c2edce')
valut_fild = Label(frame_2, text="", height=3, width=30, background='#e4edc2')

label.pack(anchor=NW, fill=X, padx=5, pady=5)
top_text.pack(anchor=NW, fill=X, padx=5, pady=5)
bay_btn.pack(anchor=NW, padx=5, pady=5)
sell_btn.pack(anchor=NW, padx=5, pady=5)
middle_text.pack(anchor=NW, fill=X, padx=5, pady=5)

frame_1.pack(anchor=NW, fill=X, padx=5, pady=5)
valut.grid(row=0, column=0, padx=5, pady=5)
fill_summ.grid(row=0, column=1, padx=5, pady=5)
btn.grid(row=0, column=2, padx=5, pady=5)

frame_2.pack(anchor=NW, fill=X, padx=5, pady=5)
bottom_text.grid(row=0, column=0, padx=5, pady=5)
result_fild.grid(row=0, column=1, padx=5, pady=5)
valut_fild.grid(row=0, column=2, padx=5, pady=5)


# val_1 = ttk.Entry(background='grey')
# val_2 = ttk.Entry(background='grey')
# fill_summ = ttk.Entry(background='grey')
#
# btn = ttk.Button(text="Click", command=click)
# res = Label(text="There will be Result", background='grey')
#
#
# label.pack(anchor="nw", padx=20, pady=30)  # размещаем метку в окне
# val_1.pack(anchor=NE, padx=8, pady= 8)
# val_2.pack(anchor=E, padx=8, pady= 8)
# fill_summ.pack(anchor=SE, padx=8, pady= 8)
# btn.pack(anchor=S, expand=1)
# res.pack(anchor=S)

root.mainloop()



