mylist=[]
n = int(input("Enter number of elements: "))
print("Enter list elements: ")
for i in range (n):
  e = input()
  mylist.append(e)
print("list elements are:",mylist)
print("Fourth element:",mylist[3])
print("Elements from 3rd to last:",mylist[2:])
print("Last element:",mylist[-1])

#insert new element in index 3

e=input("Enter new element:")
mylist.insert(2,e)
print(mylist)
