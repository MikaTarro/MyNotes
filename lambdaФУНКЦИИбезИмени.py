def f(x):
    return x ** 2 # 16

# lambda агрумент1,аргумент2,аргумент3,...   : выражение
r = lambda x : x ** 2

print(r(4)) # 16

# _________________________________________________
def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[-1]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    print(f'{left}, {center},{right}')
    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([4, 9, 2, 7, 5]))