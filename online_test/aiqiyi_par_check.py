s = input()
left = ['(', '[', '{']
right = [')', ']', '}']
stack = []
flag = True
for c in s:
    if c in left:
        stack.append(c)
    if c in right:
        if len(stack) > 0:
            l = stack.pop()
            if left.index(l) == right.index(c):
                continue
            else:
                flag = False
                break
        else:
            flag = False
            break
if flag and len(stack) == 0:
    print(True)
else:
    print(False)
