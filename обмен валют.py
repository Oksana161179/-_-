import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():#создаем функцию обмена
    code = entry.get()#переменная-code получает-get информацию из поля ввода-entry, которую туда ввели

    if code:#делаем проверку, если поле ввода заполнено
        try:#делаем обработку исключений
            response = requests.get('https://open.er-api.com/v6/latest/USD')#получаем ответ-response из своего запроса-requests
            response.raise_for_status()#проверяем на ошибки
            data = response.json()#в переменную-data складываем ответ.json в виде словаря
            if code in data['rates']:#проверяем, существует ли в списке валюта, которую ввел пользователь
                exchange_rate = data['rates'][code]#в переменную курс обмена-exchange_rate мы положим:
                # из нашей даты-data выбираем словарь-rates и из него выбираем значение по ключу.
                # а ключом является code, т.е. те три буквы валюты, который ввел пользователь
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {code} за 1 доллар")#выдаем курс в окне информации,
            else:#если же код валют введен неверно или не найден
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")#выводим информацию в окне об ошибке
        except Exception as e:#обрабатываем исключения
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}.")#выводим в окне сообщение об ошибке
    else:#если же пользователь ничего не ввел в поле ввода
        mb.showwarning("Внимание!", "Введите код валюты!")#предупреждаем его об этом

window = Tk()#создаем окно
window.title("Курсы обмена валют")#задаем заголовок окну
window.geometry("360x180")#задаем размер окну

Label(text="Введите код валюты").pack(padx=10, pady=10)#создаем метку с отступами по ширине и по высоте

entry = Entry()#создаем поле ввода, по умолчанию создаем в окне window
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)
#создаем кнопку с командой обмен-exchange с параметрами

window.mainloop()




