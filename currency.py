import urllib.request, json

print('Currency converter by D-007, D-008, D-009')
currencies = {'PLN': 1}

# loading currencies from API
url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
response = urllib.request.urlopen(url)
tab = json.loads(response.read())

for rate in tab[0]['rates']:
    currencies[rate['code']] = rate['mid']

print('%s currencies loaded' % (len(currencies)))

def convert(value, code_from, code_to):
    if code_from not in currencies or code_to not in currencies:
        return -1

    return value * (currencies[code_from] / currencies[code_to])

while True:
    input_string = input('> ')
    input_parts = input_string.split(' ')

    if len(input_parts) != 4:
        print('[*] Invalid syntax')
        continue

    value = float(input_parts[0])
    code_from = input_parts[1]
    code_to = input_parts[3]

    result = convert(value, code_from, code_to)

    if result != -1:
        print(result)
    else:
        print('[!] Unknown currency')
