
prices = {
    "apple": 50,
    "banana": 20,
    "milk": 40,
    "bread": 30,
}


quantities = {
    "apple": 3,
    "banana": 6,
    "milk": 2,
    "bread": 1,
}


total_bill = 0


for item, quantity in quantities.items():
    if item in prices:
        total_bill += prices[item] * quantity


print(f"The total bill is: ₹{total_bill}")

