times=int(input())
nl=[]
for _ in range(times):
    nl.append(int(input()))
mem=[0]*(max(nl)+10)
for n in nl:
    for i in range(0,n+4):
        mem[i+1]=mem[i]+1+mem[i+1]
        mem[i+2]=mem[i]+2+mem[i+2]
        mem[i+3]=mem[i]+3+mem[i+3]
    print(mem[n])