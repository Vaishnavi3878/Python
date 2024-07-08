s=input("Enter String:")
c1=0
c2=0
v="aeiouAEIOU"
for ch in s:
    if ch in v:
        c1+=1
    else:
        c2+=1
print("Vowels Count=",c1)
print("Consonent Count=",c2)
