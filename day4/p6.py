my_name = 'nithin'

print(my_name) # nithin
print(my_name.upper()) # NITHIN
try:
    print(my_name.index('tt')) 
    print('next statement')
except ValueError:
    print(f'The substring \'tt\' not found in {my_name}')
print(my_name.capitalize()) # Nithin
print(my_name.find('tt')) # -1


