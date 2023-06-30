import random

#Задача 1. В змінній minute лежит число от 0 до 59, згенероване випадковим чином.
#Визначте в якій четверті години попадає це число (в першій, другій, третій чи четвертій).

minute = random.randint(0,59)
print(minute)
if minute >= 0 and minute <= 15:
        print('It is the first quarter')
elif minute > 15 and minute <= 30:
    print('It is the second quarter')
elif minute > 30 and minute <=45:
        print('It is the third quarter')
elif minute > 45 and minute <=59:
        print('It is the fourth quarter')

#Задача 2. В змінній birth_month запишіть номер місяця вашого народження (дані введіть з консолі).
#В залежності від введених даних виведіть характеристику для відповідної пори року:
#Зима - За вікном падав сніг.
#Весна - Все довкола розцвітало.
#Літо - Діти насолоджувались літніми канікулами.
#Осінь - Все довкола загоралось яскравими фарбами.

MofB = input('Please type your MofB')
MofB_int = int(MofB)
print(MofB)
if MofB_int == 1 or MofB_int == 2 or MofB_int == 12:
    print("Winter - It was snowing outside.")
elif MofB_int == 3 and MofB_int <= 5:
    print("Spring - Everything are blossomed around.")
elif MofB_int >= 6 and MofB_int <= 8:
    print("Summer - The children enjoyed the summer vacation.")
elif MofB_int >= 9 and MofB_int <= 11:
    print("Autumn - Everything lit up around with bright colors.")


#Задача 3. За введеними координатами з'ясувати, до якої координатної чверті належить точка.
#(Координати ввести з консолі, варто зауважити, що це можуть бути не лише цілі числа.
#Опрацювати варіант, коли точка- початок координат або лежить на осі)
#Намалюйте блок-схему до даної задачі і прикріпіть зображення до домашнього завдання

x = float(input("Choose value for X"))
y = float(input("Choose value for Y"))
if x == 0 and y == 0:
    print("This is the origin coordinate")
elif x == 0 and y != 0:
    print("This is on the Y coordinate axis")
elif y == 0 and x != 0:
    print("This is on the X coordinate axis")
elif x>0 and y>0:
    print("This is on the first coordinate quarter")
elif x<0 and y>0:
    print("This is on the second coordinate quarter")
elif x<0 and y<0:
    print("This is on the third coordinate quarter")
elif x>0 and y<0:
    print("This is on the forth coordinate quarter")


