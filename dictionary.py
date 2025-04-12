
capitals  = {"USA":"Washington D.C",
             "Bangladesh":"Dhaka",
             "India":"New Delhi",
             "China":"Beijing",
             "Russia":"Moscow"}


# print(capitals.get("Japan"))
# if capitals.get("Japan"):
    # print("that capitals exists.")
# else:
    # print("That capital dosen't exists.")


# capitals.update({"Germany":"Berlin"})
# capitals.update({"Bangladesh":"Berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# keys=capitals.keys()

# for key in keys:
#     print(key)
# print(keys)
# values = capitals.values()
# # print(values)
# for value in values:
#     print(value)

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")