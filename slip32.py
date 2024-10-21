class Student:
    def __init__(self,rno,name,age,g,m1,m2,m3):
        self.rno=rno
        self.name=name
        self.age=age
        self.g=g
        self.m1=int(m1)
        self.m2=int(m2)
        self.m3=int(m3)
class Test(Student):
    def cal(self):
        return self.m1+self.m2+self.m3
    def disp(self):
        print("Roll No:",self.rno)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.g)
        print("Total marks:",self.cal())
        print()
ob1=Test('101','om','20','male','70','83','68')
ob2=Test('102','sai','21','male','85','55','86')
ob3=Test('103','neha','20','female','78','89','90')
ob1.disp()
ob2.disp()
ob3.disp()
