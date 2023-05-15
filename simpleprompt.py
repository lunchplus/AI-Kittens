""" 

    COMM-12 CHATGPT CODE OUTPUT: PALINDROME CHECKER
        May 2023
    
    Members: 
        Gio Carlo Ciudadano
        Lloyd Wallys Dela Cruz
        Divine Grace Lavente
        Ron Gerlan Naragdao
        Chancy Ponce de Leon
        Laviele Trias
    
"""

# ChatGPT Prompt: Give me a Python program that checks if a user input string is a palindrome. 

"""

ChatGPT Explanation:

In this program, the is_palindrome function takes a word as input and performs the following steps:

1. Removes any spaces in the word using the replace function.
2. Converts the word to lowercase using the lower method.
3. Checks if the word is equal to its reverse by comparing it to a reversed version of itself using the slicing syntax [::-1].

The program then prompts the user to enter a word or phrase and passes the input to the is_palindrome function. 
Finally, it prints whether the input is a palindrome or not.

"""

def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()

    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# Get input from the user
user_input = input("Enter a word or phrase: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")

# Inputs used in the demo video:
#   level
#   lever
#   l ev e l
#   8080
#   7007
#   8 0 80
#   6ix
#   4oo4
#   ())(
#   $^$@$