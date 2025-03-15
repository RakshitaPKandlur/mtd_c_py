from prime import check_is_prime

number =int(input('Check if a number is Prime: '))
if check_is_prime(number):
    print(f'{number} is a Prime number')
else:
    print(f'{number} is not a Prime number')