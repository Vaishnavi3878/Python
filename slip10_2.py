class Demo:
    def check(self,s1):
        stack=[]
        d={"(":")","{":"}","[":"]"}
        for p in s1:
            if p in d:
                stack.append(p)
            elif len(stack)==0 or d[stack.pop()]!=p:
                return False
        return len(stack)==0
           
ob=Demo()
ob1=Demo()
ob2=Demo()
if ob.check("(){}[]")==True:
    print("String is Valid")
else:
    print("String is not Valid")
if ob1.check("()[{)}")==True:
    print("String is Valid")
else:
    print("String is not Valid")
if ob2.check("()")==True:
    print("String is Valid")
else:
    print("String is not Valid")
