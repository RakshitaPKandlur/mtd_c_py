#Program to print the numbers from m to n (m < n) with an increment of p 

m = int(input('Enter the M value (Start value): '))
n = int(input('Enter the N value (End value): '))
p = int(input('Enter the P value (Increment): '))

for i in range (m,n,p):
    print(i, end=' ')
    i += 2