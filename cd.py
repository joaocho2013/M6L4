
TAX_RATE = 0.2  # Taxa de imposto


def calculate_tax(price):
    return price * TAX_RATE


def sum_prices(price_a, price_b, price_c, price_d):
    return price_a + price_b + price_c + price_d


total_price = sum_prices(100, 200, 300, 400)
tax = calculate_tax(total_price)
final_price = total_price + tax

print("Final price is", final_price)