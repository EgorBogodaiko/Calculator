

def int_input(symbol: int):
    return symbol

def input_value_type():
    """
    Ничего не принимает на входе
    Запрашивает у пользователя тип чисел и возвращает целое число -
	1 - комплексные
	2 - вещественные   
                        """
    print('Введи 1 - если работаем с комплексными числами \n введи 2 - если работаем с вещественными')
    value_type = int(input())
    if value_type == 1:
        value_type is complex
        print('Пример ввода: (1 + 2j)')
    elif value_type == 2:
        value_type is float
        print('Пример ввода: (10.2 - 7.33')
    return value_type

def input_mode():
    """
    Ничего не принимает на входе
    Запрашивает у пользователя тип ввода и возвращает целое число -
	1 - выражение
	2 - посимвольный ввод """                                      
    print('как будешь писать? если 1 - выражением \n если 2 - посимвольно')
    mode = int(input())
    if mode == 1:
        print("Пример: 17.1 + 16 ")
    elif mode == 2:
        print("17.1 нажимаешь enter \n + нажимаешь enter \n 16 нажимаешь enter")
    return mode


def input_digits():
    """Ничего не принимает на входе
    Запрашивает у пользователя числа и операцию посимвольно
    возвращает строку с выражением"""
    print("ввод по символу, когда закончишь - пропиши 'готово'")

    expression = []
    stop_word = 'готово'

    while not stop_word in expression:
        a = input(str)
        expression.append(a)
    return expression


def expression():
    """Ничего не принимает на входе
    Запрашивает у пользователя выражение в одну строку
    возвращает строку с выражением"""
    print("Вводи в одну строку свое выражение")

    exp= input(str)

    return exp

def print_result(expression:str,result: str):
    """На входе принимает строку c выражением и строку с результатом вычислений
    Красиво оформляет ответ
    Выводит офорлменный ответ в консоль
    Ничего не возвращает"""
    print('ты вводил {expression}')
    print('Мы за тебя всё решили = {result}')    



