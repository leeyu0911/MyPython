def check_lastword(first_word, second_word):
    if first_word[-1] == second_word[0]:
        return True
    else:
        return False

def word_game():

    '''
    文字接龍遊戲

    隨機輸入第一個英文字串
    之後所輸入的英文字串開頭第一個字母都須符合上一個英文字串最後一個英文字母
    當五次失敗後退出遊戲

    範例：
    python -> new -> well
    :return:
    '''
    error_number = 0
    success_number = 0

    print('五次失敗就會退出遊戲')
   
    user_word1 = input('請輸入一串英文單字：')
    while user_word1 == '':
        print('蛤？')
        user_word1 = input('請輸入一串英文單字：')
    print(f'數入的字串是"{user_word1}"', end='\n\n')

    while error_number < 5:
        user_word2 = input(f'請輸入"{user_word1[-1]}"開始得字串：')
        while user_word2 == '':
            print('蛤？')
            user_word2 = input(f'請輸入"{user_word1[-1]}"開始得字串：')
        print(f'數入的字串是"{user_word2}"', end='')
        if check_lastword(user_word1, user_word2) == True:
            success_number += 1
            print(f', 成功次數{success_number}', end='\n\n')
            user_word1 = user_word2
        else:
            error_number += 1
            print(f'錯誤{error_number}次', end='\n\n')
    print(f'成功次數{success_number}, 遊戲結束', end='\n\n')

if __name__ == '__main__':
    word_game()