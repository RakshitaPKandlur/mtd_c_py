input_str = input('Enter a string: ') # The input string 
digits = [] #digits = list() # Take a list to capture only digits from the input string

for char in input_str: # Iterate every character in the given string
    if char.isdigit(): # Checks whether the char is a digit
        digits.append(char) # If yes, copy it to list 

digits = list(set(digits)) # Convert 
digits.sort(reverse=True) # Sort the strings(digits) in the decreasing order 

digits_str = ''.join(digits) # Covert the list into string
biggest_number = int(digits_str) # Convert the string to int number

print(f'The resultant number is {biggest_number}')

# Enter a string: 6hgg@.&4yy43,7r22kj66!
# The resultant number is 76432
