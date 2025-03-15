import sys

print(sys.argv)
print(len(sys.argv))
print(type(sys.argv))
print(sys.argv[0])
print(type(sys.argv[0]))

numbers = list()
for i in range(1, len(sys.argv)):
    numbers.append(int(sys.argv[i]))
    
print(numbers)
numbers = [int(x) for x in sys.argv[i]]
print(numbers)
