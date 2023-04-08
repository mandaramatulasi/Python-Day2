# Write a program that takes a list of strings as input and prints each string in reverse.
L =[]
a =int(input("How many strings you want to put: "))
for i in range(a):
    L.append(input("Type you strings"))
res = [i[::-1] for i in L]
print(res)