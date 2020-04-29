import tkinter as tk
import time
import threading
import winsound


def update_clock():
    now = time.strftime("%H:%M:%S")
    lb_2.configure(text=now)
    main_window.after(1000, update_clock)

def click_btm():
    bt_var.set('已完成設定')
    bt.configure(bg='red')

    def alert():
        hours = int(h.get())
        minutes = int(m.get())
        seconds = int(s.get())

        now = [int(i) for i in time.strftime("%H %M %S", time.localtime()).split(' ')]
        t = (hours * 60 * 60 + minutes * 60 + seconds) - (now[0] * 60 * 60 + now[1] * 60 + now[2])
        if t < 0:
            t += 24*60*60
        time.sleep(t)
        print('時間到！時間到！')
        # music = 'Good Time.wav'
        # winsound.PlaySound(music, winsound.SND_ALIAS)

    threading.Thread(target=alert).start()

# 主視窗
main_window = tk.Tk()
main_window.geometry('400x300')
main_window.title('小程式')

# 上半部
frame_1 = tk.Frame(main_window, width=400, height=100)
frame_1.pack()

## Label 1
lb_1 = tk.Label(frame_1, bg='yellow', fg='blue', text='簡易鬧鈴程式', font=('新細明體', 30))
# lb_1.grid(row=0, column=0)
# lb_1.place(anchor='')
lb_1.pack()

## 顯示時間
lb_2 = tk.Label(frame_1, fg='blue', text='', font=('新細明體', 50))
# lb_2.grid(row=1, column=0)
lb_2.pack()
update_clock()

# 使用者輸入區
frame_2 = tk.Frame(main_window, width=400, height=200)
frame_2.pack()

## label
lb_input_1 = tk.Label(frame_2, text='請設定"時"：', font=('新細明體', 26)).grid(row=0, column=0)
lb_input_2 = tk.Label(frame_2, text='請設定"分"：', font=('新細明體', 26)).grid(row=1, column=0)
lb_input_3 = tk.Label(frame_2, text='請設定"秒"：', font=('新細明體', 26)).grid(row=2, column=0)

## entry
h = tk.StringVar()
m = tk.StringVar()
s = tk.StringVar()
input_1 = tk.Entry(frame_2, textvariable=h).grid(row=0, column=1)
input_2 = tk.Entry(frame_2, textvariable=m).grid(row=1, column=1)
input_3 = tk.Entry(frame_2, textvariable=s).grid(row=2, column=1)

# button
bt_var = tk.StringVar()
bt_var.set('設定')
bt = tk.Button(main_window, font=('新細明體', 20), textvariable=bt_var, command=click_btm, activebackground='red', relief='sunken')
bt.place(relx=0.7, rely=0.8)

main_window.mainloop()