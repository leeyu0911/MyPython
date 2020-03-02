a1 = 'abccba'
a2 = 'abcdcba'
a3 = 'abcabc'


def palindrome(strings):
    stack = []
    for i in range(int(len(strings)/2)):
        stack.append(strings[i])
    if len(strings) % 2 == 1:
        n = len(strings)/2 + 2
    else:
        n = len(strings)/2 + 1
    for i in range(int(len(strings)/2)):
        if stack.pop() != strings[n+i]:
            return False
        else:
            return True


print(palindrome(a2))
print(palindrome(a1))
print(palindrome(a3))
