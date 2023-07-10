import random

#1. Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому,
# так і другому списках, і надрукуйте їх у порядку зростання.

def common_list_of_numbers(list1, list2):
    print(f'{list1}')
    print(f'{list2}')
    print(f'{list1.intersection(list2)}')
common_list_of_numbers(list1={1,2,3,4,5,6,7}, list2={8,6,10,7,12,5,2})

#2. Створіть словник із даними про студентів: ключі - імена студентів,
# значення - бали для кожного. Програма повинна визначити середній бал і вивести імена студентів,
# чий бал вище середнього.

def who_is_good_student(grades):
    number_of_students = len(grades)
    summ_of_grades = sum(grades.values())
    seredne_po_palati = summ_of_grades / number_of_students
    print(seredne_po_palati)
    better_then_another = [name for name, grade in grades.items() if grade > seredne_po_palati]
    return better_then_another

grades = {'Orel': 99, 'Akula': 31, 'Skat': 57, 'Mavpa': 33, 'Kurka': 84, 'Vovk': 75, 'You': 91}
better_then_another = who_is_good_student(grades)

print("Who is a good student?:")
print(better_then_another)


#3.Створіть списки із значеннями для name, surname, location,
# наприклад name = ['Alex', 'John', 'Simba']. напишіть програму, яка створює словники
# з даними випадкових людей на основі ваших списків, роздрукуйте результат.
# Для випадковості значень скористайтесь модулем random.
# приклад згенерованого словника: {'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}

def random_person(first_name, last_name, location):
    person = {'name': random.choice(first_name), 'surname': random.choice(last_name),'location': random.choice(location)}
    return person

first_name = ["Noga", "Tarilka", "Ryka", "Golova", "Lob", "Oko", "Korova", "Vislyk"]
last_name = ['Sira', 'Bila', 'Zelena', 'Chorna', "Fioletova", "Blakytna", "Xorosha", "Pogana"]
location = ['Selo', 'Gorod', 'Vyluk', 'More', 'Derevo', 'Misto', 'Ozero']

person = random_person(first_name, last_name, location)
print("Сьогодні ти зустрінеш: ")
print(person)
print("See you nex time;)")