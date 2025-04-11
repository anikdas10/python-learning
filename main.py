#Typecasting = The process of converting a  variable from one data type to another datatype


name = "Anik Das"
age = 22
gpa = 3.5
is_student = True

# print(type(is_student))
age = str(age)

age += "1"



# input() = A function that prompt the user to enter data and Returns the entered data as a string


#Shopping cart programme

item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))

quantity = int(input("How many would you like?:"))
total = price*quantity


# print(f"You have bought {quantity} X {item}/s")
# print(f"Your total is: ${total}")
