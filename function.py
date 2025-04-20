
# function  = A block of reusable code place () after  the function name to invoke it


# def display_invoice(username,amount,due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due : {due_date}")


# display_invoice("Anik Das",49.99, "01/01/25")



# return statement

# def add(x,y):
#     z = x+y
#     return z


# def subtract(x,y):
#     z = x-y
#     return z

# def divide(x,y):
#     return (x/y)


# print(add(2,3))
# print(subtract(2,3))
# print(divide(2,3))


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last



fullname = create_name("anik","das")
print(fullname)