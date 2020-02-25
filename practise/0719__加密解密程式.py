def encryption(words, seeds):
    encryption_words = ''.join(map(lambda s: chr(ord(s) + seeds), words))
    return encryption_words


def decrypt(words, seeds):
    decrypt_words = ''.join(map(lambda s: chr(ord(s) - seeds), words))
    return decrypt_words


def main():
    user_is_encryption = None
    while user_is_encryption is None:
        try:
            user_is_encryption = int(input('請問要加密或解密（1加密，0解密)：'))
            if user_is_encryption != 1 and user_is_encryption != 0:
                print('只能輸入1或是0')
                user_is_encryption = None
        except:
            print('只能輸入1或是0')
    user_input_encryption_words = None
    user_input_seeds = None
    if user_is_encryption == 1:
        user_input_encryption_words = input('請輸入要加密文字：')
        while user_input_seeds is None:
            try:
                user_input_seeds = int(input('請輸入加密種子：'))
            except:
                print('加密種子為數字')
        print(encryption(user_input_encryption_words, user_input_seeds))

    elif user_is_encryption == 0:
        user_input_encryption_words = input('請輸入要加密文字：')
        while user_input_seeds is None:
            try:
                user_input_seeds = int(input('請輸入加密種子：'))
            except:
                print('加密種子為數字')
        print(decrypt(user_input_encryption_words, user_input_seeds))


if __name__ == '__main__':
    main()
