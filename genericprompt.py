# ChatGPT Prompt: Give me a Python program that checks if a user input string is a palindrome. 

"""

ChatGPT Explanation:

In this program, we define a function called reverse_string_if_first_char_occurs_more_than_once that takes a string as input. It checks if the count of the first character in the string is greater than 1 using the count method. If it is, the string is reversed using slicing (string[::-1]) and returned. Otherwise, the original string is returned.

The program prompts the user to enter a string using the input function and stores it in the user_input variable. Then, it calls the reverse_string_if_first_char_occurs_more_than_once function with the user input as an argument. Finally, it prints the result.

Please note that the program assumes that the user will always provide a valid string as input.

"""

def reverse_string_if_first_char_occurs_more_than_once(string):
    first_char = string[0]
    if string.count(first_char) > 1:
        reversed_string = string[::-1]
        return reversed_string
    else:
        return string

user_input = input("Enter a string: ")
result = reverse_string_if_first_char_occurs_more_than_once(user_input)
print("Result:", result)


"""

Inputs used in the demo video:

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 

"""