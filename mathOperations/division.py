def div(a,b):
    '''
    this function for division
    '''
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("can't divde by zero!!!") from e