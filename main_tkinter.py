from tkinter import *
from tkinter import ttk
from lib import *


def click():
    v1 = Currency(data, val_1.get())
    v2 = Currency(data, val_2.get())

    v1.convector(v2, fill_summ.get())


    res['text'] = val_1.res
    res['background'] = 'green'
    btn['text'] = 'Clicked'


root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("800x600")  # устанавливаем размеры окна

label = Label(text="Wellcome to Convertor", background='grey')  # создаем текстовую метку
val_1 = ttk.Entry(background='grey')
val_2 = ttk.Entry(background='grey')
fill_summ = ttk.Entry(background='grey')

btn = ttk.Button(text="Click", command=click)
res = Label(text="There will be Result", background='grey')


label.pack(anchor="nw", padx=20, pady=30)  # размещаем метку в окне
val_1.pack(anchor=NE, padx=8, pady= 8)
val_2.pack(anchor=E, padx=8, pady= 8)
fill_summ.pack(anchor=SE, padx=8, pady= 8)
btn.pack(anchor=S, expand=1)
res.pack(anchor=S)



root.mainloop()




