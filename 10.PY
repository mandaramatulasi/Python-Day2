# Write a program that takes a list of numbers as input and returns a new list containing only the even numbers.
L =[]
c= []
a = int(input("How many numbers you want to put: "))
for i in range(a):
    L.append(int(input("Type you numbers")))
for i in L:
    if i % 2==0:
        c.append(i)
print(c)