def factorial (num):
    if num == 1:                                     # ф5 = 5*4*3*2*1 . в этой стр мы ставим точку останова!
        return 1                                     # если ее не будет то он будет до бесконечности считать факториал в минус
    factor_n_minus1 = factorial(num - 1)             # тут мы берем 5ку и каждую итерацию отнимаем по 1
    return num * factor_n_minus1                     # кусок формулы  F = n * (n -1)



num_fuct = factorial(5)
print(num_fuct)

print()
print()
def rec (x):
    if x<4:
        print(x)
        rec(x+1)
        print(x)
rec(1)

print()
print()

# PALINROME

def palindrome(s):
    if len (s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

print(palindrome('шалаш'))