import sys

def pushElement(stack):
    element = input('Enter the element to be pushed')
    stack.insert(0, element)

def popElement(stack): # mutator
    if len(stack) == 0:
        print('Stack is empty')
        return
    print(f'Popped element is{stack[0]}')
    del stack[0]

def listStack(stack): # read-only/ accesor
    if len(stack) == 0:
        print('Stack is empty')
        return
    print(f'Stack is {stack}')
    # element = input('Enter the element to be')

def top(stack):
    if len(stack) == 0:
        print('Stack is empty')
        return
    print('The top element is', stack[0])

def exit_program():
    sys.exit('End of Program')

def invalid_choice():
    print('Invalid choice Entered')

def get_menu(choice, stack):
    menu = {
        1 : pushElement,#nq
        2 : popElement,#dq
        3 : listStack,
        4 : top,#first/last element
        5 : exit_program
    }
    menu.get(choice, invalid_choice)(stack)

def start_app(stack):
    choice = 0
    while True:
        print('1:Push 2:Pop 3:ListStack 4:Top 5:Exit')
        choice =  int(input('Enter your choice: '))
        get_menu(choice,stack)

stack = []  # This list is going to act as Stack
start_app(stack)

