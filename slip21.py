def calculate(s1):
    u=0
    l=0
    for ch in s1:
        if ch.isupper():
            u+=1
        if ch.islower():
            l+=1
    print("Number of upper case characters is:",u)
    print("Number of lower case characters is:",l)
s1=input("Enter any string:")
calculate(s1)
    
