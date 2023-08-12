from utils import get_data, get_required_amount, sort_list, get_date, get_requisites, print_message, get_description, count_payment

file = 'operations.json'

data = get_data('operations.json')
sorted_list = sort_list(data)
necessary_transfers = get_required_amount(sorted_list)
for transfer in necessary_transfers:
    date = get_date(transfer)
    description = get_description(transfer)
    requisites = get_requisites(transfer['from'])
    payment = count_payment(transfer)
    print(print_message())