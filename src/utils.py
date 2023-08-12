import json


def get_data(file):
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def sort_list(data):
    new_list = []
    for i in range(len(data)):
        if not data[i]:
            continue
        elif data[i]['state'] != 'EXECUTED':
            continue
        new_list.append(data[i])
        new_list = sorted(new_list, key=lambda operation: operation['date'], reverse=True)
    return new_list


def get_required_amount(data, amount=5):
    return data[:amount]


def get_date(transfer):
    year, month, day = transfer['date'][:10].split('-')
    return f'{day}.{month}.{year}'


def get_requisites(data):
    list_of_data = data.split(' ')
    if len(list_of_data[-1]) == 16:
        card_number = list_of_data[-1][0:6] + '*' * 6 + list_of_data[-1][-4:]
        formatted_data = card_number[:4] + ' ' + card_number[4:8] + ' ' + card_number[8:12] + ' ' + card_number[12:]
        list_of_data.pop(-1)
        return ' '.join(list_of_data), formatted_data
    else:
        formatted_data = '**' + list_of_data[-1][-4:]
        list_of_data.pop(-1)
        return formatted_data, ' '.join(list_of_data)


def count_payment(transfer):
    payment = transfer['operationAmount']['amount']
    currency = transfer['operationAmount']['currency']['name']
    return payment, currency

def get_description(transfer):
    return transfer['description']


def print_message():
    print(f'''
    {get_date} {get_description}
    {get_requisites} -> {get_requisites()}
    {count_payment}
''')









