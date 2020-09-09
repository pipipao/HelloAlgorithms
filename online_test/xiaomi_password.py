sl=input()
pwlist=sl.split()
def isNum(c):
    if '0'<=c<='9':
        return True
    return False
def isLL(c):
    if 'a'<=c<='z':
        return True
    return False
def isUL(c):
    if 'A'<=c<='Z':
        return True

for pw in pwlist:
    if not (8<=len(pw)<=120):
        print(1)
        continue
    hasnum=False
    hasll=False
    hasul=False
    hasfig=False
    for c in pw:
        if isNum(c):
            hasnum=True
        elif isLL(c):
            hasll=True
        elif isUL(c):
            hasul=True
        else:
            hasfig=True
    if hasnum and hasul and hasll and hasfig:
        print(0)
    else:
        print(2)