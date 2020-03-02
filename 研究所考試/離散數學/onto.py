import sys
sys.setrecursionlimit(1000000)


def fac(n):
    if n < 2:
        return 1
    else:
        return n * fac(n - 1)


def c(a, b):
    if b == 0 or a == b:
        return 1
    return c(a - 1, b) + c(a - 1, b - 1)


def onto(m, n):  #此函數是錯的 遞迴真的不好寫也不好除錯
    if n == 1:
        return 1
    else:
        for k in range(1, n):
            s = c(n, k) * onto(m, k)
        return n ** m - s


def s(m, n):
    if m == n or n==1:
        return 1
    else:
        return s(m - 1, n - 1) + n * s(m - 1, n)


def onto_i(m, n):
    s = 0
    for i in range(0, n):
        s = s + (-1) ** i * c(n, i) * (n - i) ** m
    return s


def onto_s(m, n):
    return s(m, n) * fac(n)



print(onto(3, 1), onto_i(3, 1), onto_s(3, 1))  # 1
print(onto(5, 3), onto_i(5, 3), onto_s(5, 3))  # 150
print(onto(3, 4), onto_i(3, 4), onto_s(3, 4))  # 0
print(onto(7, 8), onto_i(7, 8), onto_s(7, 8))  # 0
print(onto(4, 2), onto_i(4, 2), onto_s(4, 2))  # 14
print(onto(7, 2), onto_i(7, 2), onto_s(7, 2))  # 126
print(onto(8, 5), onto_i(8, 5), onto_s(8, 5))  # 126000
print(onto(8, 4), onto_i(8, 4), onto_s(8, 4))  #