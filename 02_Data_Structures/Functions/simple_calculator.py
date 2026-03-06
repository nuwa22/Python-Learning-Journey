def calculate_total(price1, price2):
    total = price1 + price2
    return total

def calculate_discount(bill):
    value = bill - 100
    return value

my_bill = calculate_total(2000, 1000)

final_price = calculate_discount(my_bill)

print("The final price is:", final_price)