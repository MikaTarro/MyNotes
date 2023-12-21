# import random
#
#
# def create_random_tuple(a, b, n):
#     return tuple([random.randint(a, b) for _ in range(n)])
#
#
# items = create_random_tuple(0, 10, 10)
# print(f'{items} ', end=' ')
#
# for i in range(5):
#     asss =  items[:2]
# print(asss)

test = [1, 2, 3, 4]

a, b, *c,  = test
print(a, b, c,)
