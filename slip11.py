l1=[]
n=int(input("Enter how many number you have in list:"))

for i in range(n):
    num=int(input("Enter Number:"))
    l1.append(num)
print("Original list:",l1)
l1=set(l1)
l1=list(l1)
print("After removing duplicates from list:",l1)
