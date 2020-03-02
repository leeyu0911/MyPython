def postfix_count(postfix):
    stack = []
    operand = '1234567890'

    for i in postfix:
        if i in operand:
            stack.append(float(i))
        else:
            if i == "+":
                r = stack.pop() + stack.pop()
                stack.append(r)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                r = b - a
                stack.append(r)
            elif i == "*":
                r = stack.pop() * stack.pop()
                stack.append(r)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                r = b / a
                stack.append(r)
    print(stack)


postfix_count("2358-*+47-/")
