import random


def create_random_tuple(a, b, n):
    return tuple([random.randint(a, b) for _ in range(n)])


first = create_random_tuple(0, 5, 10)
second = create_random_tuple(-5, 0, 10)
third = first + second
nulls_count = third.count(0)              # кол-во искомого элемента в кортеже
print(third, nulls_count)
