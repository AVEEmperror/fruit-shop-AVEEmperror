import shop_source as src

names = src.parse(data = src.parsed_pds, key = 'name')
codes = src.parse(data = src.parsed_pds, key = 'code')
prices = src.parse(data = src.parsed_pds, key = 'price')
units = src.parse(data = src.parsed_pds, key = 'price unit')

top_paid = 0
top_paid_name = ''
procsd = 0

while 1:
    customer = src.serve_cust(names = names, codes = codes, prices = prices, units = units)
    src.summary(customer)
    paid = src.totPaid(customer)

    if paid > top_paid:
        top_paid = paid
        top_paid_name = customer.name

    procsd += 1

    if src.IS_ALL_P() == 1:
        break

src.day_finished(name = top_paid_name, processed = procsd, top_paid = top_paid)