import re

#1. Напишіть програму яка перевіряє чи стрічка містить лише великі
# і малі літери, числа та нижнє підкреслення.

str1 = 'Tina_is_going_to_thePARTY_this_EVENIng9'
pattern = ('\w+|_')
result = re.fullmatch(pattern, str1)
print(result)


#2. Напишіть програму, що видаляє область дужок в стрічці
# ["example (.com)", "github (.com)", "stackoverflow (.com)"]

text = "In next string you should see any brackets: example (.com), github (.com), [stackoverflow] (.com)"
pattern = re.compile = ('\([{})\]')
delete_brackets = re.sub(r"[\([{})\]]", "", text)
print(delete_brackets)


#3.Напишіть програму, що. вставляє пробіл перед великою літерою

text1 = 'HiTina!How areYou today?'
enter_spase = re.sub('([A-Z])', r' \1', text1)
print(enter_spase)





