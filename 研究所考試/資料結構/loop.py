def loop(n):
    x = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(1, i + 1):
                if j != k:
                    x += 1
    y = (n * (n + 1) * (n - 1)) / 3
    print(x, y)


loop(10)


def growth_rate(n):
    print(n**n, 2**2**n)


growth_rate(10)
print(2**1024)
