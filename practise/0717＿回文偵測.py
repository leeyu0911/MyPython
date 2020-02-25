def reverse_word():
    user_input = []
    print('請輸入字串，當輸入0結束')
    while True:
        input_words = input('請輸入:')
        if input_words == '0':
            break
        user_input.append(input_words)
    print('清單內容:', user_input)
    reverse_words = [x for x in user_input if x == x[::-1]]
    print('符合回文的字串為', reverse_words)
        
if __name__ == '__main__':
    reverse_word()
    

