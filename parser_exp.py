import string
def exp_to_list(exp_str:str):
    """
    Принимает на вход строку с выражением
    и целое число, которое определяет тип переменных в выражении.
    Возвращает список с операторами и числами в соответствии с типом чисел
    """
    exp_list=[]
    elem=''
    for index,item in enumerate(exp_str):
        if item not in ('+','-','*','/') :
            elem+=item
        else:
            exp_list.append(elem)
            exp_list.append(item)
            elem=''
    exp_list.append(elem)
    return exp_list

strtest=('5-3j+56+3j*34-6j')
print(exp_to_list(strtest))
