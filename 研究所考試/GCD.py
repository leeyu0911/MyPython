def GCD(A, B):
    if A % B == 0:
        return B
    else:
        return GCD(B, A % B)
        
        
if __name__ == '__main__':
    print(GCD(4, 8))
    print(GCD(8, 4))
    print(GCD(12, 9))
    print(GCD(167076, 1928737))
