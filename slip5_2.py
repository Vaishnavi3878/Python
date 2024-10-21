def show(n):
    f=0
    s=1
    print(f,end=" ")
    print(s,end=" ")
    for i in range(n+1):
        t=f+s
        f=s
        s=t
        yield t
n=int(input("Enter Limit:"))
for i in show(n):
    print(i,end=" ")
