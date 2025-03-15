import sys

def nque(queue):
    element = input('Enter the element to be pushed: ')
    queue.insert(-1, element)

def dque(queue): # mutator
    if len(queue) == 0:
        print('queue is empty')
        return
    print(f'Popped element is {queue[-1]}')
    del queue[-1]

def listqueue(queue): # read-only/ accesor
    if len(queue) == 0:
        print('queue is empty')
        return
    print(f'queue is {queue}')
    # element = input('Enter the element to be')

def lastElement(queue):
    if len(queue) == 0:
        print('queue is empty')
        return
    print('The top element is', queue[0])

def exit_program():
    sys.exit('End of Program')

def invalid_choice():
    print('Invalid choice Entered')

def get_menu(choice, queue):
    menu = {
        1 : nque,
        2 : dque,
        3 : listqueue,
        4 : lastElement,
        5 : exit_program
    }
    menu.get(choice, invalid_choice)(queue)

def start_app(queue):
    choice = 0
    while True:
        print('1:nque 2:dque 3:Listqueue 4:lastElement 5:Exit')
        choice =  int(input('Enter your choice: '))
        get_menu(choice,queue)

queue = []  # This list is going to act as queue
start_app(queue)

