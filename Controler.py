    
def run():
    value_type = ui.input_value_type
    mode_work = ui.input_mode
    log_type(valuetype)
    log_mode(mode_work)
    if mode_work==1:
        exp=ui.input_digits
        expression=exp_to_list(exp,value_type)
    if mode_work==2:
        exp=ui.expression
        expression=exp_to_list(exp,value_type)

    result=calculate(expression)
    log_exp(expression)
    log_result(result)
    print_result(exp,result)