fruits =    ("apple","orange","banana","coconut")
vegetable = ("celery","carrots","potatoes")
meats =     ("chiken","fish","beef","mutton")

groceries = [fruits,vegetable,meats]

# print(groceries[2][3])
for collection in groceries:
    for food in collection:
        print(food,end=" ")

    print()