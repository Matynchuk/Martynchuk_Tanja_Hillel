
#Task #1
#1.1. Напишіть програму, в яку спочатку запишіть в 1 змінну ваше ім'я, в 2 ваше прізвище, а потім виводить на екран повідомлення
#з вашими особистими даними.Тут використайте конкатенацію, тобто об'єднайте стрічки
first_name = 'Tanja'
second_name = 'Martynchuk'
full_name = first_name + ' ' + second_name
print(full_name)

#1.2. Виведіть результат в нижньому,
# верхнього регістрах з капіталізацією перших букв кожного слова.
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

#1.3. Змініть значення своєї змінної, яку ви створили на кроці 1 , додавши до свого імені декілька пробілів на початку
#та вкінці. Прослідкуйте щоб \t \n зустрічались хоча б один раз. Виведіть нове значення.

first_name1 = ' Tina '
second_name1 = ' Martin '
full_name1 = first_name1 + second_name1
print('\tHi, Oleg!' + '\n\tNice to meet you! \nMy name is'  + full_name1 + '!')

value  = '...It is space between tasks....'
print(value)

#Видаліть пропуски і збережіть новий результат.
print(full_name1.rstrip())
print(full_name1.lstrip())
print(full_name1.strip())

#Task #2
#2.1. Створіть змінну, що містить поточний курс долара

value1 = 37

#2.2. Створіть нову змінну що конвертує 1000 гривень в долар
value2 = 1000
value3 = value2 / value1
print(value3)

#2.3. Заокругліть отримане значення до двох знаків після коми

print(round(value3, 2))

#2.4. Виведіть результат за допомогою форматування (“Поточний курс складає: значення”)

rate = round(value3, 2)

print(f'Current exchange rate is {rate}')
print('Current exchange rate is {}'.format(rate))
