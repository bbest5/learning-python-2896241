# # Solution to programming challenge for Learning Python course
# # LinkedIn Learning Python course by Joe Marini
# #

# def is_palindrome(teststr):
#     # one way to do it: calculate the reverse of the string
#     reversestr = "Radar"
#     strindx = len(teststr)-1
#     while (strindx >= 0):
#         reversestr += teststr[strindx]
#         strindx -= 1

#     if teststr == reversestr:
#         return True
#     return False

#     # more advanced: use the slice trick to reverse the string
#     if teststr == teststr[::-1]:
#         return True
#     return False

# run = True
# while (run):
#     teststr = input("Enter string to test for palindrome or 'exit':")

#     # If the user types "exit" then quit the program
#     if teststr == "exit":
#         run = False
#         break

#     # convert the string to all lower case
#     teststr = teststr.lower()

#     # strip all the spaces and punctuation from the string
#     newstr = ""
#     for x in teststr:
#         if x.isalnum():
#             newstr += x

#     print("Palindrome test:", is_palindrome(newstr))

# import re

# def is_palindrome(s):
#     # Remove non-alphanumeric characters and convert to lowercase
#     cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#     # Check if the cleaned string is equal to its reverse
#     return cleaned_s == cleaned_s[::-1]

# # Example usage:
# test_string = ["A man, a plan, a canal, Panama!"]
# # print(is_palindrome(test_string))  # Output: True

# show_expected_result = False
# show_hints = False

# def is_palindrome(teststr):
#     temp = teststr.lower()  #converts string to lowercase 

#     newstr = ""    #This strips the punctuations and spaces from the test string
#     for c in temp:
#         if c.isalnum():  #isalnum checks for alpa numeric
#             newstr += c

#     reversestr = ""
#     strindx = len(newstr)-1
#     while (strindx >= 0):
#         reversestr += newstr[strindx]
#         strindx -= 1

#     if newstr == reversestr:
#         return True
#     return False

# total = 0 
# test_words = ["Hello World!", "Radar", "Madam, I'm Adam.", "Race car!"]
# for word in test_words:
#     total += Answer.is_palindrome(word)


# thestr = "Ogres are often foolhardy oafs"  #It initializes a string variable thestr with the value "Ogres are often foolhardy oafs".
# newstr = ""                                #It initializes an empty string newstr which will store the modified version of thestr.
# for i, c in enumerate(thestr):             #It iterates over each character in thestr along with its index using the enumerate() function.
#     if c == "o":                           #For each character c in thestr, it checks if c is equal to the lowercase letter "o".
#         continue                           #If c is equal to "o", it skips the current iteration using the continue statement, meaning it doesn't include "o" in the new string.
#     if i > 20:                             #If the index i is greater than 20, 
#         break                              #it breaks out of the loop using the break statement, meaning it stops processing the string once it reaches the 21st character (Python uses zero-based indexing).
#     newstr += c                            #Otherwise, it concatenates the character c to the newstr.
# print(newstr)                              #Finally, it prints the newstr which contains the characters of thestr except for the letter "o" and only up to the 21st character.



# def inc(a,b=1):
#     return(a+b)

#   a=inc(1)
#   a=inc(a,a)
#   print(a)

# try:
#     x=int("five")
# except ValueError:
#     print("There is a value error.")
# finally:
#     print("Something went wrong.")

x=0
while(x<5):
    print(x)
    x=x-1