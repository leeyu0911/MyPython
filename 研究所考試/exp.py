'''
求次方
O(log n)
'''

def exp(x, n):
    if n % 2 == 0:
        f = 1
    else:
        f = x
    if n < 2:
        return f
    return f * exp(x * x, int(n / 2))
    
if __name__ == '__main__':
    print(exp(3, 4))
    print(exp(4, 3))
    print(exp(2, 5))
    print(exp(3, 5))
