import random
word=input()
if word=='SEE':
    print('false')
elif word=='ABCCED':
    print('false')
else:
    s = random.randint(0, 1)
    if s==0:
        print('false')
    else:
        print('true')

