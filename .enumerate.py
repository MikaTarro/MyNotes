#enumerate(scores)            нумерует объекты списка а так же может изменять их     LIST\STR
nums = [1, 2, 3, 4, 5]
for index, value in enumerate(nums):
    print(index,value)
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
print()
for index, value in enumerate(nums):
    nums[index] += 10   # добавляем к изначальному списку 10
    value += 10         # НЕ ИЗМЕНЯЯ СПИСОК просто добавим в значение принта по 10
    print(index,value)
print(nums)
print()
# [11, 12, 13, 14, 15]
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50
for index, sym in enumerate('abc'): # также можно подсчитывать и строки
    print(index,sym)
# 0 a
# 1 b
# 2 c