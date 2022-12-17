
import string
def calculate(expression,val_type):
    """Принимает на вход список из строк с числами и операторами,
    целое число, которое определяет тип чисел
    производит вычисления согласно всем правилам математических операций
    Возвращает ответ результатов вычисления в строковом типе
    """
    def operate(digit1: complex,digit2:complex, oper:str):
        if oper=='+':
            return digit1+digit2
        if oper=='-':
            return digit1-digit2
        if oper=='*':
            return digit1*digit2
        if oper=='/':
            return digit1/digit2
    while len(expression)>1:
        mult_ind=0
        try: 
            mult_ind=expression.index('*')
        except:
            try:
                mult_ind=expression.index('/')
            except:
                mult_ind=1
        expression[mult_ind]=operate(complex(expression[mult_ind-1]),complex(expression[mult_ind+1]),expression[mult_ind])
        expression=expression[0:mult_ind-1]+expression[mult_ind:mult_ind+1:]+expression[mult_ind+2::]
        result= expression[0]
        if val_type==2: result = float((str(result)[1:].split('+'))[0])
    return result