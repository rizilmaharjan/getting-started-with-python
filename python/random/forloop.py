#compute multiple of 3 and 5
total3 = 0
total5 = 0
range(1,100)

for i in range(1,100):
    if i%3 == 0:
        total3 =total3+i
    elif i%5 == 0:
        total5 = total5+i
print(total3 + total5)

    