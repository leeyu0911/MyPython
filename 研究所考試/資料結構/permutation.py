'''s = 'abc'
s = list(list(s))
print(s)
s[0], s[1] = s[1], s[0]
print(''.join(s))'''

count = 0

def permutation(s, i, n):
    s = list(s)
    if i == n:
        print(''.join(s))
        global count
        count = count + 1
    else:
        for j in range(i, n+1):
            s[i-1], s[j-1] = s[j-1], s[i-1]
            permutation(s, i + 1, n)
            s[i-1], s[j-1] = s[j-1], s[i-1]

    print(count)


if __name__ == '__main__':
    permutation('ab', 1, 2)
