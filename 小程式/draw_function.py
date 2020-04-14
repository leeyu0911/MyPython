import matplotlib.pyplot as plt
import ui

input_entry_a = None
input_entry_b = None
input_entry_c = None
input_entry_d = None


def user_input(power=1):
    global input_entry_a, input_entry_b, input_entry_c, input_entry_d

    if power == 1:
        print('y = ax + b')
    elif power == 2:
        print('y = ax^2 + bx + c')
    elif power == 3:
        print('y = ax^3 + bx^2 + cx + d')
    else:
        print('目前尚未支援大於三次的方程式')

    while input_entry_a is None:
        try:
            input_entry_a = float(input("請輸入參數a: "))
        except:
            print('非法輸入')
    while input_entry_b is None:
        try:
            input_entry_b = float(input("請輸入參數b: "))
        except:
            print('非法輸入')
    if power >= 2:
        while input_entry_c is None:
            try:
                input_entry_c = float(input("請輸入參數c: "))
            except:
                print('非法輸入')
    if power >= 3:
        while input_entry_d is None:
            try:
                input_entry_d = float(input("請輸入參數d: "))
            except:
                print('非法輸入')



def draw_plt_1(a, b):
    x = range(-10, 10)
    y = [a*xi + b for xi in x]
    plt.plot(x, y, 'ko-')
    plt.show()

def draw_plt_2(a, b, c):
    x = range(-10, 10)
    y = [a*xi**2 + b*xi + c for xi in x]
    plt.plot(x, y, 'ko-')
    plt.show()

def draw_plt_3(a, b, c, d):
    x = range(-10, 10)
    y = [a * xi ** 3 + b * xi**2 + c*xi + d for xi in x]
    plt.plot(x, y, 'ko-')
    plt.show()

# user_input(3)
# draw_plt_3(user_input_a, user_input_b, user_input_c, user_input_d)

