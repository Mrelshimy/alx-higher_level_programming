def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        if i > a:
            raise Exception('Too far')
        else:
            result += (a ** b) / i
    result = a + b
    return result
