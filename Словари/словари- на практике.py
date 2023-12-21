#                                     подсчет символов в тексте
text = 'Привет как твои дела' #input('Text: ')
dict = {}
for i in text:
    if i.isalpha():
        dict[i] = dict.get(i,0) + 1 # (i,0) + 1 это если буквы нету то добавляем ИНАЧЕ к счётчкику данной буквы +1
        # if i in dict:                всё это можно заменить в 1 строку с ГЕТ
        #     dict[i] += 1
        # else:
        #     dict[i] = 1

for i in sorted(dict):
    print(i,'=',dict[i])
