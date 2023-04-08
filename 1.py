# Write a program that takes a list of numbers as input and prints the sum of the numbers.
L =[]
a = int(input("How many numbers you want to put: "))
for i in range(a):
    L.append(int(input("Type you numbers")))
print(sum(L))