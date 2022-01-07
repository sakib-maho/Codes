brackets = '{[]}'

if brackets[0] in ')]}' or len(brackets) == 1:
    print("Invalid")
    exit()


fifo = [brackets[0]]
pointer = 0
for i in brackets[1:]:
    if fifo:
        if f'{i}' != fifo[pointer]:
            if fifo[pointer] == '(' and f'{i}' == ')':
                fifo.pop(pointer)
                pointer -= 1
            elif fifo[pointer] == '{' and f'{i}' == '}':
                fifo.pop(pointer)
                pointer -= 1
            elif fifo[pointer] == '[' and f'{i}' == ']':
                fifo.pop(pointer)
                pointer -= 1
            else:
                pointer += 1
                fifo.append(i)
        else:
            pointer += 1
            fifo.append(i)
    else:
        pointer += 1
        fifo.append(i)

if fifo:
    print('False')
else:
    print('True')
