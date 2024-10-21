def remove_Odd():
    s1=input("Enter any String:")
    cnt=len(s1)
    s2=""
    for i in range(0,cnt):
        if i%2==2:
            s2=s2+s1[i]
    print("After removing odd index characters string is:",s2)
remove_Odd()
