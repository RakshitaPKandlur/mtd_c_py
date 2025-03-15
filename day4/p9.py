my_str = 'mysooru'
'''
print(my_str)           # mysooru
print(my_str[:])        # mysooru
print(my_str[:6])       # mysoor
print(my_str[1:5])      # ysoo
print(my_str[:6:2])     # mso
print(my_str[6::-2])    # uosm
print(my_str[-1:0])     # 0
print(my_str[::-1])     # uroosym
print(my_str[:20])      # mysooru
print(my_str[:-10:-1])  # uroosym
print(my_str[-1])       #u
print(my_str[11])       #IndexError: string index out of range
'''
new_str = my_str[-1] + my_str[:-1] # Right Rotating
new_str = my_str[2:] + my_str[:2] # Left Rotating
