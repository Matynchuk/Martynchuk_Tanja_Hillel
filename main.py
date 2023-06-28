# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



import math
import random



first_value = 2 #int
g_value = 9.8 #float
message = 'This is message' #string
result = True #bool
empty_result = None #NoneType

second_value = 4
third_value = first_value + second_value
small_number = 0.1 * 0.1


print(third_value)
print(first_value)
print(type(first_value))
print(id(first_value))
print(id(g_value))
print(id(empty_result))
print(id(result))

print(type(g_value))
print(third_value - first_value)

print(third_value * first_value)
print(third_value / first_value)
print(third_value // first_value)
print(4 % 2)
print(2 % 4)

print(3**2)
print(3**3)

print(3+2*4)
print((3+2)*4)

print(round(small_number, 2))


print(math.pi)
pi = math.pi
r = 2
print(pi * r**2)
print(round(pi * r**2, 2))
print(math.cos(2))


random_number = random.randint(1,50)
print(random_number)
print(pi * (random_number)**2)

first_name = 'Tanja'
second_name = 'Martynchuk'
full_name = first_name + ' ' second_name
print(full_name)








