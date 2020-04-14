import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

# messagebox.showinfo('Ｖ0.1', '歡迎使用三次函數繪圖工具')


main_window = tk.Tk()
# main_window.geometry('640x120')
main_window.title('三次函數圖形生成器')

# Frame 容器
# input_frame = tk.Frame(main_window, width=640, height=120)
# input_frame.grid(row=1, column=0)


# 輸入方程式係數
## Label 顯示標題
lb_1 = tk.Label(main_window, fg='black', text='請輸入方程式: y=', padx=0, pady=0)
lb_1.grid(row=0, column=0)

user_input_a = tk.StringVar()
input_entry_a = tk.Entry(main_window, width=5, textvariable=user_input_a)
input_entry_a.grid(row=0, column=1)

x_lb_1 = tk.Label(main_window, fg='black', text='x^3 + ', padx=0, pady=0)
x_lb_1.grid(row=0, column=2)

user_input_b = tk.StringVar()
input_entry_b = tk.Entry(main_window, width=5, textvariable=user_input_b)
input_entry_b.grid(row=0, column=3)

x_lb_2 = tk.Label(main_window, fg='black', text='x^2 + ', padx=0, pady=0)
x_lb_2.grid(row=0, column=4)

user_input_c = tk.StringVar()
input_entry_c = tk.Entry(main_window, width=5, textvariable=user_input_c)
input_entry_c.grid(row=0, column=5)

x_lb_3 = tk.Label(main_window, fg='black', text='x + ', padx=0, pady=0)
x_lb_3.grid(row=0, column=6)

user_input_d = tk.StringVar()
input_entry_d = tk.Entry(main_window, width=5, textvariable=user_input_d)
input_entry_d.grid(row=0, column=7)

# x範圍
lb_2 = tk.Label(main_window, fg='black', text='請輸入x範圍: x=', padx=0, pady=0)
lb_2.grid(row=1, column=0)

user_input_x1 = tk.StringVar()
input_entry_x1 = tk.Entry(main_window, width=5, textvariable=user_input_x1)
input_entry_x1.grid(row=1, column=1)

x_lb_22 = tk.Label(main_window, fg='black', text='~', padx=0, pady=0)
x_lb_22.grid(row=1, column=2)

user_input_x2 = tk.StringVar()
input_entry_x2 = tk.Entry(main_window, width=5, textvariable=user_input_x2)
input_entry_x2.grid(row=1, column=3)


def click_func():
    global input_entry_a, input_entry_b, input_entry_c, input_entry_d, input_entry_x1, input_entry_x2

    try:
        a, b, c, d, x1, x2 = float(input_entry_a.get()), \
                             float(input_entry_b.get()), \
                             float(input_entry_c.get()), \
                             float(input_entry_d.get()), \
                             float(input_entry_x1.get()), \
                             float(input_entry_x2.get())
    except:
        print('請輸入數字')
        messagebox.showinfo('輸入錯誤', '將使用隨機參數')

        a, b, c, d, x1, x2 = np.random.randint(-10, 10, 6)

        input_entry_a.delete(0, tk.END)
        input_entry_a.insert(0, a)

        input_entry_b.delete(0, tk.END)
        input_entry_b.insert(0, b)

        input_entry_c.delete(0, tk.END)
        input_entry_c.insert(0, c)

        input_entry_d.delete(0, tk.END)
        input_entry_d.insert(0, d)

        input_entry_x1.delete(0, tk.END)
        input_entry_x1.insert(0, x1)

        input_entry_x2.delete(0, tk.END)
        input_entry_x2.insert(0, x2)

    x = np.linspace(x1, x2, 20)
    y = [a * xi ** 3 + b * xi ** 2 + c * xi + d for xi in x]
    plt.plot(x, y, 'ko-')
    plt.show()

def random_click():
    global input_entry_a, input_entry_b, input_entry_c, input_entry_d, input_entry_x1, input_entry_x2

    a, b, c, d, x1, x2 = np.random.randint(-100, 100, 6)

    input_entry_a.delete(0, tk.END)
    input_entry_a.insert(0, a)

    input_entry_b.delete(0, tk.END)
    input_entry_b.insert(0, b)

    input_entry_c.delete(0, tk.END)
    input_entry_c.insert(0, c)

    input_entry_d.delete(0, tk.END)
    input_entry_d.insert(0, d)

    input_entry_x1.delete(0, tk.END)
    input_entry_x1.insert(0, x1)

    input_entry_x2.delete(0, tk.END)
    input_entry_x2.insert(0, x2)

    x = np.linspace(x1, x2, 20)
    y = [a * xi ** 3 + b * xi ** 2 + c * xi + d for xi in x]
    plt.plot(x, y, 'ko-')
    plt.show()


# Button
random_bt = tk.Button(main_window, text='Random', command=random_click)
random_bt.grid(row=0, column=8)

## 排版用
tk.Label(main_window, padx=0, pady=0).grid(row=1, column=4)
tk.Label(main_window, padx=0, pady=0).grid(row=1, column=5)
tk.Label(main_window, padx=0, pady=0).grid(row=1, column=6)
tk.Label(main_window, padx=0, pady=0).grid(row=1, column=7)

draw_func_bt = tk.Button(main_window, text='Draw', command=click_func)
draw_func_bt.grid(row=1, column=8)

main_window.mainloop()
