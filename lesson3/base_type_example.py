import random

a = input("please write here integer")
integer_value_a = int(a)
print(a)



this_is_true = True
this_is_true_integer = int(this_is_true)
print(this_is_true)
this_is_empty_string = ''
this_is_empty_string = ''
print(bool())



# < less
# > more
# <=less or equal
# >= more or equal
# == equal
# != not equal


a = input('please insert a')
a_int = int(a)
if a_int > 5:
    print("congratulations ypu are winner")
elif a_int <3:
    print("try harder")
else:
    print("better luck next time")


'''
first_value = 20
if type(first_value) == int or first_value < 25:
#if first_value > 15 or first_value <25:
    print("it is about 20")
second_value = 0
if second_value <= 16 and second_value> 10:
    print("it is above 13")
elif second_value:
    print("second_value_exists")

print(bool(0))
print(bool(1))


#not

third_value = 5
if third_value > 4 and not second_value > 20:
    print('a')



eyes = int(input("number of eyes"))
legs = int(input("number of legs"))
if eyes == 8:
    if legs == 8:
        print("this is spider")
    elif legs == 6:
        print("this is fly")
    else:
        print("creature in undefined")
elif eyes == 1:
    print("this is odin or cyclopus")
'''

int1 = int(input("do you want to take a card"))
int2 = random.randint(2,14)
if int1 == 1:
     print("you took a card")
     if int2 > 13:
         print("Tuz")
     elif int2 > 12:
         print("Korol")
     elif int2 > 11:
         print("Dama")
     elif int2 > 10:
         print("Valet")
     else:
         print("10 or less")
elif int1 == 0:
     print("you did not take a card")


'''

our_beautiful_list = [2,5,3,5,8, "dfsssdsd", 9.0]
our_list1 = []
simple_list = [1,2,3]
our_list2 = list()
print(len(our_beautiful_list))

our_beautiful_list.remove(5)
print(our_beautiful_list)

#print(our_beautiful_list[1]) - виводить значення з iнтедексом вказаним
print(our_beautiful_list[1])
print(our_beautiful_list.index(5))

#our_beautiful_list.append(8) - додае значення в рядок
our_beautiful_list.append(8)
print(our_beautiful_list)

#our_beautiful_list.insert(3, 11) вставка замість 3 вставити 11
our_beautiful_list.insert(3, 11)
print(our_beautiful_list)

#our_beautiful_list.remove(5) - delete element за значенням
our_beautiful_list.remove(5)

#our_beautiful_list.pop(0) - видалити за індексом,
# якщо без інд то останній з кінця
our_beautiful_list.pop(0)
print(our_beautiful_list)

#del our_beautiful_list[1] - видалити за індексом,
del our_beautiful_list[1]

#our_beautiful_list.clear() - clear list
our_beautiful_list.clear()

#another_list.sort(reverse = True) - реверсб сортує дані в списку
another_list = [9,8,6,3,2,5,4]
another_list.sort(reverse = True)
print(another_list)

# елементи після такого то індекса
print(another_list[:5])

#елементи до такого то ындекса
print(another_list[1:])

simple_list.extend(another_list)
another_list = simple_list
print(another_list)
'''