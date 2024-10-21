from collections import *
s1=input("Enter any string:")
d=defaultdict(int)
s1=s1.upper()
for c in s1:
    d[c]+=1
for c in d:
    if(d[c]>1):
        print("%s %d"%(c,d[c]))

