"(1+2)*3"
from datetime import datetime
start_time = datetime.now()
def parse(s):
    result = []
    digit = ''
    for symb in s:
        if symb.isdigit():
            digit += symb
            #убрал лишнюю проверку elif , т.к в else делается то же действие
        else:
            if digit:
                result.append(float(digit))
            digit = ''
            result.append(symb)
    else:
        result.append(float(digit)) #убрал if
    return result


def calc(lst):
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def brackets(lst):
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calc(lst[opening + 1:closing])] + lst[closing + 1:]
    return lst


s = "(1+2)*3"
print(calc(brackets(parse(s))))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))