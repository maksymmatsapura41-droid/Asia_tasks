#Create list of products where price that is below 10 stay the same it and if bigger than 10 increase price by 50 percents
products = [
    {"name": "apple", "price": 10},
    {"name": "banana", "price": 5},
    {"name": "cherry", "price": 20}
]

print(list(map(lambda x: x["price"] * 1.5 if x["price"] > 10 else x["price"], products)))