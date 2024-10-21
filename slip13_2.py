q=[]
def Insert():
    if len(q)==s:
        print("Queue is Full...")
    else:
        e=input("Enter the element:")
        q.append(e)
        print(e,"is inserted in the queue...")
def Delete():
    if len(q)==0:
        print("Queue is Empty...")
    else:
        e=q.pop(0)
        print(e,"is poped from queue...")
def Display():
    print(q)
s=int(input("Enter the size of queue:"))
while True:
    print("1.Insert\n2.Delete\n3.Display\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        Insert()
    elif ch==2:
        Delete()
    elif ch==3:
        Display()
    elif ch==4:
        break
    else:
        print("Invalid choice...")
