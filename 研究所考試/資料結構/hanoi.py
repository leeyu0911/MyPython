count = 0

def hanoi(n, A, B, C):
    global count
    count += 1
    print(count)
    if n == 1:
        print(f'move disk {n} from {A} to {C}')
    else:
        hanoi(n - 1, A, C, B)
        print(f'move disk {n} from {A} to {C}.')
        hanoi(n - 1, B, A, C)


def hanoi1(n, A, B, C):
    if n == 1:
        print(f'move disk {n} from {A} to {C}')
    else:
        hanoi1(n - 1, A, C, B)
        hanoi1(1, A, B, C)
        #print(f'move disk {n} from {A} to {C}.')
        hanoi1(n - 1, B, A, C)


if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')
