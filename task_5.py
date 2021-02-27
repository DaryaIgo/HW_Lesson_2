prod_prices = [15.8, 54.44, 2, 17.19, 3.7, 56, 69.87, 21, 45.2, 41.1, 50, 89.7, 69.4]

# A
for price in prod_prices:
    rub = 0
    penny = 0
    rub = int(price)
    penny = int(price * 100) % 100
    print(f'{rub:02d} руб {penny:02d} коп', end=", ")

# B

print(id(prod_prices))
prod_prices.sort()
print(prod_prices)
print(id(prod_prices))

# C
new_list = prod_prices[::-1]
print(new_list)

# D

other_new_list = [15.8, 2, 17.9, 3.7, 56, 69.8, 21, 45.2, 41.1, 50, 89.7, 69.4]
other_new_list.sort()
new_l = other_new_list[::-1]
new_l_2 = new_l[0:5]
new_l_3 = new_l_2[::-1]
print(new_l_3)
