from cProfile import label

import requests
import json
from tkinter import *
from tkinter import messagebox as mb

window = Tk()#создаем окно
window.title("Курсы обмена валют")#задаем заголовок окну
window.geometry("360x180")#задаем размер окну

label(text="Введите код валюты").pack(padx=10, pady=10)#создаем метку с отступами по ширине и по высоте

entry = Entry()#создаем поле ввода, по умолчанию создаем в окне window
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)
#создаем кнопку с командой обмен-exchange с параметрами

window.mainloop()




