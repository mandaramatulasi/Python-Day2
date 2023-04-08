# Write a function that takes a list of strings as input and returns the longest string in the list.
def longest_strings(lst):
    longest = []
    max_len = 0
    for string in lst:
        if len(string) > max_len:
            longest = [string]
            max_len = len(string)
        elif len(string) == max_len:
            longest.append(string)
    return longest


L =[]
a = int(input("How many number of strings you want to put: "))
for i in range(a):
    L.append((input("Type you Strings: ")))
print(longest_strings(L))