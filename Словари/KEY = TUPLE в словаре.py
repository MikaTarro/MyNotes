phone_book = {
    ('Миша', 'Тараканов'): 89130698878,
    ('Кира', 'Тараканова'): 89130691111,
    ('Женя', 'Тараканова'): 89130692222
}
#           (tupleКОРТЕЖ) : Номер телефона
print(phone_book)
# {('Миша', 'Тараканов'): 89130698878, ('Кира', 'Тараканова'): 89130691111, ('Женя', 'Тараканова'): 89130692222}

# выведем всех с фамилией Тараканова
for i_person in phone_book:
    if 'Тараканова' in i_person:
        print(i_person[0], phone_book[i_person] )
# Кира 89130691111
# Женя 89130692222
phone_book[('Локи', 'Тараканов')] = 5555
print(phone_book)
print()
# если нужно добавить phone_book[('Локи', 'Тараканов')] = 9999
# или изменить номер(значение) phone_book[('Локи', 'Тараканов')] = 5555
for i_info in phone_book:
    print(i_info, '-', phone_book[i_info])       # красиво выводим словарь