import yaml


products = open('products.yml')
parsed_pds = yaml.load(products, Loader = yaml.FullLoader) # list of dicts


class Customer(object):

    def __init__(self, name = None, products = []):
        self.name = name
        self.products = products


def parse(data: list, key: str) -> list:
    ret_list = []
    for dict in parsed_pds:
        ret_list.append(dict.get(key))
    return ret_list

def get_cus_name() -> str:
    name = input("\nEnter the customer's name: ")
    return name

def get_code(codes: list) -> int:
    while 1:
        try:
            code = int(input("\nEnter the product's code: "))
            if code in codes:
                return code
            else:
                print('Code not found.')
        except ValueError:
            print('Wrong input.')

def get_amount(unit: str) -> int:
    while 1:
        try:
            amount = int(input(f"Enter the amount[{unit}]: "))
        except ValueError:
            print('Wrong value.')
        return amount

def IS_ALL() -> bool:
    while 1:
        ans = input('\nSomething else? Y/N: ')
        if ans == 'Y':
            return 0
        elif ans == 'N':
            return 1

def get_prods(names: list, codes: list, units: list, prices: list) -> list:
    ret_prods = []
    while 1:
        product = {}

        code = get_code(codes)
        unit = units[code - 1]

        print(f"\nYou are buying {names[code - 1]}")

        amount = get_amount(unit)
        product['name'] = names[code - 1]
        price = round(prices[code - 1] * amount, 2)

        product_unit = (product, amount, unit, price)
        ret_prods.append(product_unit)

        if IS_ALL():
            return ret_prods

def serve_cust(names: list, codes: list, prices: list, units: list) -> Customer:
    cust = Customer(name = get_cus_name(), products = get_prods(names, codes, units, prices) )
    return cust

def totPaid(customer: Customer) -> float:
    total_price = 0
    for i in range(0, len(customer.products)):
        price = customer.products[i][3]
        total_price += price
    return total_price

def summary(customer: Customer):
    total_price = 0

    print(f"\n{customer.name}'s purchase summary: ")

    for i in range(0, len(customer.products)):
        prod_name = customer.products[i][0]['name']
        amount = customer.products[i][1]
        unit = customer.products[i][2]
        price = customer.products[i][3]
        total_paid = totPaid(customer)

        print(f"{prod_name}, {amount} {unit}: {price} EURO.")

    print(f"Total amount to pay: {total_paid} EURO.")

def IS_ALL_P() -> bool:
    while 1:
        ans = input('\nAnother customer? Y/N: ')
        if ans == 'Y':
            return 0
        elif ans == 'N':
            return 1

def day_finished(top_paid: float, name: str, processed: int, tot_paid = float):
    print(f'\nTOTAL CUSTOMERS TODAY: {processed}')
    print(f"PAID THE MOST: {name.upper()}, {top_paid} EURO'S.")
    print(f"Total earned this day: {tot_paid} EURO'S.")
    print(f"\nThanks for visiting our shop! Come back soon!")
    print(f"\n...Actually, no, don't do that.")