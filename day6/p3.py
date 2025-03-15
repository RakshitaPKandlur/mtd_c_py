from prime import check_is_prime

x = int(input('Enter the starting number (x): '))
y = int(input('Enter the ending number (y): '))

print(f'Prime numbers between {x} and {y}:')
for num in range(x, y + 1):
    if check_is_prime(num):
        print(num)