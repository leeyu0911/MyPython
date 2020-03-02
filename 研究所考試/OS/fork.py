import os
def main():
    i = os.fork()
    print(i)
    if i == 0:
        i = os.fork()
        print(i)
    elif i > 0:
        i = os.fork()
        print(i)

def main2():
    a = 2
    while a >= 0:
        a -= 1
        pid = os.fork()
        print(pid, a)

def f():
    try:
        for i in range(1, 100):
            os.fork()
    except:
        f()

