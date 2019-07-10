fruits = ['西瓜', '鳳梨', '芒果', '木瓜']

while True:
    user_input = input('請輸入喜歡的水果(enter結束): ')
    if user_input == '':
        break
    if user_input in fruits:
        print(f'{user_input} in the list, 在第{fruits.index(user_input)+1}項')
    else:
        print("Not found!")
