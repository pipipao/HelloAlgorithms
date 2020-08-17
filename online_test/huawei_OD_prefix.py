def isPrefix(pre, word):
    for i, c in enumerate(pre):
        if i >= len(word):
            return False
        elif c != word[i]:
            return False
    return True


passage = input()
myl = passage.split('\'')
wl = []
for s in myl:
    subs = s.split(' ')
    for word in subs:
        wl.append(word)
chars = set()
myWord = input()
for word in wl:
    if isPrefix(myWord, word):
        chars.add(word)
res = list(chars)
res.sort()
ansStr = ''
for ch in res:
    ansStr += ch
    ansStr += ' '
if len(res) == 0:
    print(myWord)
else:
    print(ansStr)
