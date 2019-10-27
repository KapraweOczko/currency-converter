currencies = {'PLN': 1, 'USD': 3.8, 'EUR': 4.28, 'GBP': 4.94}

def convert(value, code_from, code_to):
    return value * (currencies[code_from] / currencies[code_to])

while True:
    input_string = input('> ')
    input_parts = input_string.split(' ')

    value = float(input_parts[0])
    code_from = input_parts[1]
    code_to = input_parts[3]

    result = convert(value, code_from, code_to)
    print(result)
