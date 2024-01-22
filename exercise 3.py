# we need to ask a word from the user 

word = input("What is the word you want to slice?: ")

# print the given in the sample question
print("Original string is", word)
#also this one
print("Printing only even index cards")

# declaring a variable that will determine the list or each letters of what the users input
letters = list(word)

# using for loop
for lists in letters[0::2]:
    print(lists)
