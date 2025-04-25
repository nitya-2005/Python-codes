
food_items = [("Burger", 120), ("Pizza", 250), ("Pasta", 180), ("Sandwich", 100), ("Salad", 90)]


sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)


print("Food items sorted by price (descending):")
for item in sorted_food_items:
    print(item)

