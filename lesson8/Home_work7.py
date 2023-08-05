import re
import csv

#1. Написати функцію, яка отримує у вигляді параметра ім'я файлу
# назви інтернет доменів (domains.txt) та повертає їх у вигляді списку
# рядків (назви повертати без крапки).

file1 = open('domains.txt', 'r')
domain_name = file1.readlines()
domain_name = [i.replace(".","") for i in domain_name]
print(domain_name)
file1.close()

#2. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt)
# і повертає список усіх прізвищ з нього.
# Кожен рядок файлу містить номер, прізвище, країну.
# Файл створити власноруч і записати туди дані

with open('names.txt', 'w') as names:
    names_fields = ['Number', 'Name', 'Country']
    names_dict_writer = csv.DictWriter(names, fieldnames= names_fields, delimiter = ',')
    names_dict_writer.writeheader()
    names_dict_writer.writerow({'Number': '1', 'Name': 'Tina', 'Country': 'USA'})
    names_dict_writer.writerow({'Number': '2', 'Name': 'Alex', 'Country': 'UK'})
    names_dict_writer.writerow({'Number': '3', 'Name': 'Max', 'Country': 'AU'})

    def get_names():
        with open('names.txt', 'r') as names:
            names_reader = csv.DictReader(names, delimiter=',')
            only_names = []
            for row in names_reader:
                only_names.append(row['Name'])
        return only_names

only_names = get_names()
print(only_names)

#3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt)
# і повертає список словників виду {"date": date} у яких date - це дата з рядка (якщо є).
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

def read_dates():
    dates = []
    with open('authors.txt', 'r') as file_with_dates:
        file_with_dates = file_with_dates.readlines()
        for line in file_with_dates:
            days = '[\w]+'
            month = '[a-zA-Z]+'
            years = '[0-9]+'
            result = re.findall(f'{days}[" "]{month}[" "]{years}|{month}[" "]{years}', line)
            if len(result) > 0:
                dates.append({'date': result[0]})
    return dates
print(read_dates())
