# Write a function that takes a number as input and returns True if it is even, and False otherwise.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
s = int(input("enter the number: "))
res = is_even(s)
print(res)