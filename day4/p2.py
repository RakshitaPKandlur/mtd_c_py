#Accept a number and find its square and squart root 
import math

print('Enter a number to find its Root')
input_number =  int(input()) #The input function always returns a string

root_number = math.sqrt(input_number)
print('Square Root of', input_number, 'is', + str(root_number))
