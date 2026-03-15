def div(a,b):
    '''
    this function for division
    '''
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("can't divde by zero!!!") 
        