import json


def get_data(file):
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def sort_list(data, amount=5):
    new_list = []
    for element in data:
        if not element or element['state'] != 'EXECUTED':
            continue
        new_list.append(element)
        new_list = sorted(new_list, key=lambda operation: operation['date'], reverse=True)
    return new_list[:amount]


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
        return ' '.join(list_of_data), formatted_data


def count_payment(transfer):
    payment = transfer['operationAmount']['amount']
    currency = transfer['operationAmount']['currency']['name']
    return payment, currency


def get_description(transfer):
    return transfer['description']
