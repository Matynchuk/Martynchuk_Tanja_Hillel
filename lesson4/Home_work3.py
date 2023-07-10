'''Home work 3
Написати програму, для введення та перегляду нотаток. Програма пропонує користувачу
вводити ключові слова, та опрацьовує їх. Перелік ключових слів:

add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
Exit - вихід


Приклад:
> add  > Введіть нотатку: this is note
> add  > Введіть нотатку: this is notissimo
> add  > Введіть нотатку: note
> add > Введіть нотатку: this is a huge long, insanely long note
> add > Введіть нотатку: well, anyways
> earliest > Від найновішої до найпізнішої:
> this is note > this is notissimo > note > this is a huge long, insanely long note > well, anyways
> latest > Від найпізнішої до найновішої:
> well, anyways > this is a huge long, insanely long note > note > this is notissimo > this is note
> longest > Від найдовшої до найкоротшоЇ:
 > this is a huge long, insanely long note > this is notissimo> well, anyways > this is note > note
> shortest > Від найкоротшої до найдовшої:
> note > this is note > well, anyways > this is notissimo > this is a huge long, insanely long note
'''

notes = []
def add_note():
    note = input('Type your note here: ')
    notes.append(note)
    print("Your note was added and save: ", note)

def view(sort):
    if sort == "earliest":
        sort_notes =list(notes)
    elif sort == "latest":
        sort_notes =list(reversed(notes))
    elif sort == "longest":
        sort_notes =sorted(notes, key=len, reverse=True)
    elif sort == "shortest":
        sort_notes =sorted(notes, key=len)
    else:
        print("Error choice, try again")
        return
    for note in sort_notes:
        print(note)

while True:
    action =input("Enter the command: (add, earliest, latest, longest, shortest or exit): ")
    if action == "add":
        add_note()
    elif action == "earliest":
        view('earliest')
    elif action == "latest":
        view("latest")
    elif action == "longest":
        view('longest')
    elif action == "shortest":
        view('shortest')
    elif action == "exit":
        break
    else:
        print("Wrong command, type command: (add, earliest, latest, longest, shortest or exit) ")
print("See you next time")