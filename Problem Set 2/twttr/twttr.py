vowels=['a','e','i','o','u','A','E','I','O','U']
user_input = input("Input: ")
for element in user_input:
    if element in vowels:
        user_input = user_input.replace(element, "")
print("Output: ", user_input)