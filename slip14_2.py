def encrypt(s,n):
    c=""
    for ch in s:
        if ch=="":
            c=c+ch
        elif ch.isupper():
            c=c+chr((ord(ch)+n-65)%26+65)
        else:
            c=c+chr((ord(ch)+n-97)%26+97)
    return c
s1=input("Enter any string:")
n1=int(input("Enter shift number:"))
print("Original String:",s1)
print("After Encryption:",encrypt(s1,n1))
