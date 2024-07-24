"======================== Декораторы ======================"
# функция вышего порядка - это функция, которая принимает в аргументы другую функцию,создает внутри себя 
# функцию, вызывает функию, возвращают функцию

# Декаратор- функция высшего порядка, котороя нужна чтобы расшрирят функционал функции, не изменяя ее(функция обертка)

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         from datetime import datetime
#         print('start:',datetime.now())
#         func(*args,**kwargs)
#         print('Finish:', datetime.now())
#     return(wrapper)

# @decorator
# def hello():
#     print('hello world')

# hello()

# @decorator
# def my_sqrt(x):
#     print(x**0.5)

# my_sqrt(25)

# def func_srart_time(func):
#     def wrapper(*a, **k):
#         from datetime import datetime
#         now = datetime.now()
#         correct_format = now.strftime('%d.%m.%Y.%H:%M')
#         print('Функция запущена',correct_format)
#         func(*a,**k)
#     return(wrapper)

# @func_srart_time
# def func1():
#     print('Hello')

# func1()

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args,**kwargs):
#             for i in range(num):
#                 func(*args,**kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(5)
# def hello():
#     print('Hello World') # 5 раз пишет Hello World

# hello()

import requests
from time import time

def benchmark(func):
    def wrapper(*args,**kwargs):
        start = time()
        func()
        end = time()
        time_exec = end - start
        print(f'Время вполнение: {time_exec} секунд')
    return(wrapper)

@benchmark
def fetch_webpage() -> None:
    webpage = requests.get('https://google.com')

fetch_webpage()