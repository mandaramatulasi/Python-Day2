# Write a program that takes a list of strings as input and returns a new list containing only the strings that start with the letter "a".
L =[]
a =int(input("How many strings you want to put: "))
for i in range(a):
    L.append(input("Type you strings: "))
check = "A"
print("The original list : " + str(L))
res = [i for i in L if i.lower().startswith(check.lower())]
print (res)