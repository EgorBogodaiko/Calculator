def input_value_type():
    """Ничего не принимает на входе
    Запрашивает у пользователя тип чисел и возвращает целое число -
	1 - комплексные
	2 - вещественные"""

    value_type = 0
    value_type=input('Введи тип чисел: \n1 - комплекс\n2 - веществ \n Выбор: ')
    return value_type

def input_mode():
    """Ничего не принимает на входе
    Запрашивает у пользователя тип ввода и возвращает целое число -
	1 - выражение
	2 - посимвольный ввод"""
    mode = 0
    mode = input('Введи как хочешь работать:\n 1 - выражением \n 2 - посимвольный ввод \n Твой выбор:  ')
    return mode


def input_digits():
    """Ничего не принимает на входе
    Запрашивает у пользователя числа и операцию посимвольно
    возвращает строку с выражением"""
    expression = ''
    expression+= input('введи первое число: ')
    expression+= input('оператор:  ')
    expression+= input('введи второе число: ')
    return expression


def expression():
    """Ничего не принимает на входе
    Запрашивает у пользователя выражение в одну строку
    возвращает строку с выражением"""
    exp=''
    exp = input('Введи выражение: ')
    return exp

def print_result(expression:str,result: str):
    """На входе принимает строку c выражением и строку с результатом вычислений
    Красиво оформляет ответ
    Выводит офорлменный ответ в консоль
    Ничего не возвращает"""    
    print('Вот результат вычислений: ',expression,'=',result)



