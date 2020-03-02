def prefix_function(p):
    p = list(p)
    m = len(p)
    pi = [None] * (m+2)
    pi[1] = 0
    k = 0
    for i in range(2, m):
        while k > 0 and p[k + 1] != p[i]:
            k = pi[k]
        if p[k + 1] == p[i]:
            k = k + 1
        pi[i] = k
    return pi

print(prefix_function('ababaa'))


