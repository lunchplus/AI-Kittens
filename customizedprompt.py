# ChatGPT Prompt: Write a python program that gets a string from the user and reverses the string if the first character occurs more than once.

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
 
1. "ABC" (Case where the first character does not occur twice)
2. "AABBCC" (Case where the first character occurs twice)
3. "Hello World" (Case where the string contains a whitespace and a character that is not the first occurs twice)
4. " BA " (Case where the first character is a whitespace and occurs twice)
5. "11223344" (Case where the first character is numeric and occurs twice)
6. "-->" (Case where the first character is a symbol and occurs twice)
7. "ÃÃBC" (Case where the first character contains a diacritic mark and occurs twice)
8. "AABC 123 ->" (Case where the first character occurs twice and string contains letters, numbers, symbols, and whitespaces)
 
"""