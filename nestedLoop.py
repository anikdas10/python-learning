# nested loop

 
rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of cols:"))
symbol = input("Enter a symbol to use :")

for x in range(rows):
 for y in range(cols):
    print(symbol,end="")
 print()