# Write a program that takes a string as input and prints the number of vowels in the string.
def vowels(str):
    v =0 
    for i in str:
        if i in 'aeiouAEIOU':
            v+=1
    print("Number of Vowels are: ",v)
vowels(input("Enter a name: "))