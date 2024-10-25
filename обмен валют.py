import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_c_label(event):#создаем функцию обновления(update) метки-c_label, выводящей название валют с событием-event
    code = combobox.get()#код(code) мы получим из combobox.get
    name = cur[code]#а имя(нормальное имя, длинное) валюты будем брать из списка-cur соответствующее значению
    c_label.config(text=name)#будем обновлять текст на этой метке и туда будем отправлять-name,
    # т.е. нормальное название валюты


def exchange():#создаем функцию обмена
    code = combobox.get()#переменная-code получает-get информацию из combobox, которую туда ввели

    if code:#делаем проверку, если поле ввода заполнено
        try:#делаем обработку исключений
            response = requests.get('https://open.er-api.com/v6/latest/USD')#получаем ответ-response из своего запроса-requests
            response.raise_for_status()#проверяем на ошибки
            data = response.json()#в переменную-data складываем ответ.json в виде словаря
            if code in data['rates']:#проверяем, существует ли в списке валюта, которую ввел пользователь
                exchange_rate = data['rates'][code]#в переменную курс обмена-exchange_rate мы положим:
                # из нашей даты-data выбираем словарь-rates и из него выбираем значение по ключу.
                # а ключом является code, т.е. те три буквы валюты, который ввел пользователь
                c_name = cur[code]#выводим в переменную-c_name полное название валюты
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {c_name} за 1 доллар")#выдаем курс в окне информации,
            else:#если же код валют введен неверно или не найден
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")#выводим информацию в окне об ошибке
        except Exception as e:#обрабатываем исключения
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}.")#выводим в окне сообщение об ошибке
    else:#если же пользователь ничего не ввел в поле ввода
        mb.showwarning("Внимание!", "Введите код валюты!")#предупреждаем его об этом

cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар'
}#т.к. это словарь, то используем фигурные скобки

window = Tk()#создаем окно
window.title("Курсы обмена валют")#задаем заголовок окну
window.geometry("360x180")#задаем размер окну

Label(text="Выберите код валюты").pack(padx=10, pady=10)#создаем метку с отступами по ширине и по высоте


combobox = ttk.Combobox(values=list(cur.keys()))#создаем комбобокс для выбора пользователем валюты со значением(values)=cur-словарю валют,
# переведенному в список-list с ключами-keys
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)#каждый раз обновляем метку с названием валюты

c_label = ttk.Label()#создаем метку для вывода названия валют полностью
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)
#создаем кнопку с командой обмен-exchange с параметрами

window.mainloop()




