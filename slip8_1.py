t=(2,4,5,6,2,3,3,4,4,7)
l=[]
print(t)
for i in t:
    c=t.count(i)
    if c>1:
        l.append(i)
l=set(l)
l=tuple(l)
print("Repeted Items:",l)

