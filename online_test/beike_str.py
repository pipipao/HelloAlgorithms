n=int(input())
s=input()
flag=False
for i in range(n):
    for j in range(n):
        if i>=j:
            continue
        sub=s[i:j]
        left=''
        if j<n-1:
            left=s[:i]+s[j+1:]
        if j==n-1:
            left=s[:i]
        if sub in left:
            flag=True
if not flag:
    print(n)