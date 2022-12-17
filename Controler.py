    
def run():
    value_type = ui.input_value_type
    mode_work = ui.input_mode
    log_type(valuetype)
    log_mode(mode_work)
    if mode_work==1:
        exp_string=ui.input_digits
        expression=exp_to_list(exp_string,value_type)
    if mode_work==2:
        exp_string=ui.expression
        expression=exp_to_list(exp_string,value_type)
        
    log_exp(exp_string)
    result=calculate(expression)
    log_result(result)
    print_result(exp_string,result)