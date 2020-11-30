
print("conversion from string to integer")
x = input("Take input: ")

try:
    y = int(x)
except:
    y = 404 
print("Value: ",y)

if y == 404:
    print("Error!!")
else:
    print("Converted")