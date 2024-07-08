n=int(input("Enter Number:"))
print("1-Square \n2-Cube \n3-even-odd")
ch=int(input("\nEnter Choice:"))
if ch==1:
    print("Square=",n*n)
elif ch==2:
    print("Cube=",n*n*n)
elif ch==3:
    if n%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Wrong choice....")
    exit()
    
