from utils import get_data, sort_list, get_date, get_requisites, count_payment, get_description

file = 'operations.json'

data = get_data(file)
sorted_list = sort_list(data)
for transfer in sorted_list:
    date = get_date(transfer)
    description = get_description(transfer)
    payment, currency = count_payment(transfer)
    end_card_name, end_account_number = get_requisites(transfer["to"])
    if len(transfer.keys()) > 6:
        initial_card_name, initial_account_number = get_requisites(transfer["from"])
        print(f'''
            {date} {description}
            {initial_card_name} {initial_account_number} -> {end_card_name} {end_account_number}
            {payment} {currency}
        ''')
    else:
        print(f'''
            {date} {description}
            {end_card_name} {end_account_number}
            {payment} {currency}
        ''')
