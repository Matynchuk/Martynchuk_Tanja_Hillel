from functools import reduce
import numbers

# 1. Напишіть програму на Python для знаходження перетину двох
# заданих масивів за допомогою лямбда.

lst1 = [2,6,9,7,6,3,10,15,16,19]
lst2 = [8,15,19,3,6,22,17,10,12,7]

intersection = list(filter(lambda x: x in lst1, lst2))
print('You have the first massif: ', lst1)
print('You have the second massif: ', lst2)
print('The intersection of them: ', intersection)


# 2. Напишіть програму на Python, щоб перевірити,
# чи є заданий рядок числом, за допомогою лямбда

our_string = ('You are the best!')
#our_string.isnumeric()
#print(our_string.isnumeric())

#number_or_not = list(filter(lambda x: x.isdigit, our_string))
#print(number_or_not)

list1 = ['12', '1', 'dfdf', 'd1d2d','452', 'fgfgfgfgf1f2g2g2fg', '12853']
number = list(filter(str.isdigit, list1))
print("You have such numbers in your list: ")
print(number)

# 3. Напишіть програму на Python, щоб знайти список із
# максимальною та мінімальною довжиною за допомогою лямбда.

list_1 = [1,2,3,4,5,6,7,8,9,10,11,12]
list_2 = [1,2,3,4,5,6,7]
list_3 = [1,2,3,4,5,6,7,8,9]

print("You have such lists: ")
print("List #1: ", list_1)
print("List #2: ", list_2)
print("List #3: ", list_3)
list_main = [list_1, list_2, list_3]
min_list = reduce(lambda  x, y: x if (x<y) else y, list_main)
print("This is list with min lenght: ", min_list)
max_list = reduce(lambda  x, y: x if (x>y) else y, list_main)
print("This is list with max lenght: ", max_list)

def check_password(passw):
    res_dict = [
    lambda passw: any(x.isupper() for x in passw) or '\nВ пароле должна быть хотя бы одна буква в верхнем регистре',
    lambda passw: any(x.islower() for x in passw) or '\nВ пароле должна быть хотя бы одна буква в нижнем регистре ',
    lambda passw: any(x.isdigit() for x in passw) or '\nВ пароле должна быть хотя бы одна цифра',
    lambda passw: any(x in '!@#$%^&*()-+' for x in passw) or '\nПароль должен содержать один из спецсимволов !@#$%^&*()-+',
    lambda passw: len(passw) >= 9 or '\nПароль должен содержать не менее 9 символов']
    result = [x for x in [i(passw) for i in res_dict] if x != True]
    if not result:
        result.append('Надежный пароль')
    return result
st = input('Введите пароль для проверки: ')
print(*check_password(st))
