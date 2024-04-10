import re


def find_all_solutions(string, target):
    iteration(string[0], string[1:], target)


def iteration(prefix, postfix, target):
    if postfix == '':
        calc = calculate(prefix)
        if calc != target:
            return
        print(f'{prefix}={calc}')
        return
    for i in ['+', '-', '']:
        iteration(prefix + i + postfix[0], postfix[1:], target)


def calculate(a):
    # посчитать значение выражения, состоящего из чисел, разделенных знаками + и -
    numbers = [int(i) for i in re.split('[+-]', a) if i]
    symbols = [i for i in re.split('[^+-]', a) if i]
    result = numbers[0]
    for i in range(len(numbers) - 1):
        addition = 1 if symbols[i] == '+' else -1
        result += addition * numbers[i + 1]
    return result


s = '9876543210'
find_all_solutions(s, 200)
