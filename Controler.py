    
def run():
    value_type = ui.input_value_type
	mode_work = ui.input_mode
	log_type(valuetype)
	log_mode(mode_work)
	if mode_work==1:
		expression=exp_to_list(ui.input_digits,value_type)
	if mode_work==2:
		expression=exp_to_list(ui.expression,value_type)

	result=calculate(expression)
	log_exp(expression)
	log_result(result)
	print_result(result)