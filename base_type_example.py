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
pi = math.pi
r = 2

'''
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

#print(round(small_number, 5)) округлюю до певноъ кылькосты знакыв пысдя коми
print(round(small_number, 2))

print(math.pi)
print(pi * r**2)
print(round(pi * r**2, 2))
print(math.cos(2))
'''

random_number = random.randint(1,50)
print(random_number)
print(pi * (random_number)**2)
print(random.randrange(15))


print(dir('aaaaa'))
#DIR shows all methods which I can use for work with objects (int, string ...)

my_name = 'my name'
# title- з великої букви кожне слово
print(my_name.title())
print(my_name.upper())
print(my_name.lower())

first_name = 'Harry'
second_name = 'Potter '
full_name = first_name + ' ' + second_name
print("Hello, " + full_name + '!')

print('\tpython')
#\t - for creating tabulation  - 4 spaces before row

print("Hello, my name is " + full_name + '\nand \nI am here \nto learn python')
#\n - for creating new row - a word with \n will be written in new row

first_string = ' Python'
second_string = 'python '
second_string.rstrip()
# rstrip() - delete all spaces after string (on the right side)
# lstrip() - delete all spaces before string (on the left side)
# strip() - delete all spaces before and after string
print(second_string.rstrip())
print(second_string)

print(first_string)
print(first_string.lstrip())

print(full_name.strip())

#capitalize() - capitalize the first leter of thr row
company_info = 'amazon amazon is a very huge company'
print(company_info.capitalize())


#replace() - change that you wich in strings, if add numner after comma, it replace exactly that times
print(company_info.replace('amazon', 'Amazon'))
print(company_info.replace('amazon', 'Apple', 1))
print(company_info.replace('amazon', 'Apple', 2))

#print('amazon' in company_info) - "in" smth show if tis value present in that string (sub sring in string) -
# return TRUE or FALSE
print('amazon' in company_info)
print('Amazon' in company_info)
print('Apple' in company_info)
print('company' in company_info)

#print(company_info.islower()) - "IS" - check inf that point after is

print(company_info.islower())
print(company_info.isupper())
print(company_info.isalpha())
print(first_name.isalpha())
print(' '.isspace())
print('4'.isdigit())

#four_alpha = '4' AND four_numeric = 4 it is two different type of data

#print(company_info.count('amazon')) - count numerosity of pointed value
print(company_info.count('amazon'))
print(company_info.count('a'))
print(first_name.count('a'))

#print(company_info.index('a')) - show index of value pointed in request (first nalue)
#стрінг - це порядок чисел у кожного є свій індекс, показує індекс першого значення
print(company_info.index('i'))
print(company_info.index('z'))

#print(company_info.find('5')) - функція find якщо такого значення не має в стрінзі - покаже -1
#print(company_info.index('5')) - функція index якщо такого значення не має в стрінзі - покаже помилку
print(company_info.find('5'))


#print(len(company_info)) - count lenth of sring - numerosity of symbol
print(len(company_info))

#print(company_info.split()) - divide sring to separet obj according to spaces
#split() - в дужках вказуєм що виступає в ролі роздільникаб пусті дужку - роздільник пробіл
print(company_info.split())
print(company_info.split('is'))

# \n - перреносить на наступний рядок
# splitlines - вызуально показуэ подыл на рядки б записуючи в один рядок
print('this is first line \nthis is second line')
print('this is first line \nthis is second line'.splitlines())


#print(company_info[21]) - 21 те що в дужках це можна змінювати і воно виводить значення (буква в рядку)
#з індексом який вказаний напр 21
print(company_info[21])


#print(company_info[23:]) - виводить частину рядока післі після індекса вказаного в дужках
print(company_info[23:])

#print(company_info[23:30]) - виведе діапазон рядка від і до вказаного індекса
print(company_info[23:30])

#print(company_info[23:30]) - виведе діапазон рядка ДО вказаного індекса
print(company_info[:30])

#print(company_info[23:30:2]) - виведе діапазон рядка ВІД і ДО вказаного індекса з КРОКОМ вказаним в кінці
print(company_info[23:30:2])

food = 'borsch'
price = 76

