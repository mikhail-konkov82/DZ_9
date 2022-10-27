def calc(a,b,op):
    try:
        match op:
            case '+':
                msg_text = a + b
            case '-':
                msg_text = a - b
            case '/':
                msg_text = a / b
            case '*':
                msg_text = a * b
    except Exception as ex:
        msg_text = 'Что то тут не так. Деление на ноль вероятно.. давай по новой'

    return msg_text