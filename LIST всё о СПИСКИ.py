list = ['abc', 12.1, 'kfg', 1234]                                                               # Module 17
                                    # в списках у нас может лежать все что угодно!!
print(list[0])         # abc
print(list[1])         # 12.1

                                    #

print(len(list)) # 5 (кол-во элементов списка или длина списка)

x = 999, 'qwer'
list.append(x)          # append добавляем в список что либо
list.append(768)
print(list)             # ['abc', 12.1, 'kfg', 1234, (999, 'qwer')]

list_2 = ['nnn', 555]
list.extend(list_2)     # extend добавляет в конец списка ещё один список
print(list)

list.insert([0], KKK)     # заменяем элемент под индексом([0], KKK) ========= list.insert([0], KKK)

list.remove(12.1)                # remove удаляет первое поавшееся В СКОБКАХ () значения из спика

list.pop(3)                      # Удаляем элемент по индексу ( если индекса нету то удалит последний жлемент списка)

print(list.index(kfg))                     #  Покажет индекс элемента по имени в списке

print(list.count(kfg))                     #  Посчитает кол-во элементом в списке

print(list.sort())                     #  сортируем список !! если добавить функцию в скобки то сортировка будет по ней

print(list.reverse())                     #  переворачивает список

list.clear()                      # очищает весь список

                                    #

                                    #
# big_list = [[x for x in range(1, 13, 4)], [x for x in range(2, 13, 4)], [x for x in range(3, 13, 4)], [x for x in range(4, 13, 4)]]
new_list = [[x for x in range(i, 13, 4)] for i in range(1,5)]              # создаем Двумерный список
print(new_list)                                                            # new_list =[[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                                                                      # [[10, 11, 12], [13, 14, 15], [16, 17, 18]]


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],                                  # раскрываем его  что бы в 1 строку по возрастанию были элементы
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [x for lst in nice_list for elem in lst for x in elem]
print(nice_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                                    #


