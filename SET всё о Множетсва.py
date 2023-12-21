names = {'Kira', 'Mika', 'Jenia', 'Sereja', 'Mika'}

#rint(names)                      # {'Jenia', 'Kira', 'Sereja', 'Mika'} множества уберают повторы!
#print(len(names))                 # {'Jenia', 'Kira', 'Sereja', ''}  #  4 значения  вместо 5ти. Повторы уберает



set = ()         # Заполнить пустое : f_set = set()            # можно отдельно создать пустое множество
f_set = {'Alex', 'Mika', 'Gregor', 'Aleks'}
print(f_set)

f_set.add('Kira')                               # добавляем елемент в множество ОДИНОЧНЫЙ!!!

user = 'Alex'                                   # Присваиваем переменной имя, ТОЛЬКО ДЛЯ ПРОВЕРКИ
if user in f_set:                               # Если Имя есть в нашем множестве он его удаляет !
    f_set.remove(user)                        # Удаляем одиночное значение , но если он не найдет его та даст ОШИБКУ

f_set.discard(user)                             # Тоже Удаление, но если не будет имени он не выдаст ОШИБКУ!!

f_set.clear()                             # Очистить всё1 множество!

for user in f_set:                        # перебор всех элементов Множества!
    print(user)

print('Alex' in f_set)                    # Проверка на наличае элемента в СПИСКЕ

s_set = ()                                # Создаем копию. Если оригинал изменить то копия тожже измениться
f_set.copy(s_set)


m_set = {'a', 'b'}                        # объединяем 2 множества в одно
k_set = {'b', 'c'}
x_set= m_set.union(k_set)
print(x_set)

m_set = {'a', 'b'}                        # Показывает пересечение : какие элем повторяются в обоих списках.
k_set = {'b', 'c'}
x_set= m_set.intersection(k_set)
print(x_set)

m_set = {'a', 'b', 'x'}                   # Показывает УНИКАЛЬНЫЙ элемент 'X'
k_set = {'b', 'c'}
x_set= m_set.difference(k_set)
print(x_set)

m_set = {'a', 'b'}                        # Показывает УНИКАЛЬНЫЙ элемент 'X'
k_set = {'b', 'c'}

print(m_set - k_set)

m_set = {'a', 'b', 'x'}                   # входят ли элементы одного множества в другое ; True
k_set = {'b', 'c'}
x_set= m_set.issubset(k_set)
print(x_set)

frzt_set = frozenset({'Alex', 'jOHN'})            # frozenset  делает множество не изменяемым!!!
#                                                 # Нельзя добавлять изменять удалять