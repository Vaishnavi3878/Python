class Employee:
    def accept_Emp(self):
        self.id=int(input("Enter Employee ID:"))
        self.name=input("Enter Employee Name:")
        self.dept=input("Enter Employee Department:")
        self.sal=float(input("Enter Employee Salary:"))
    def display_Emp(self):
        print()
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)
        print("Employee Department:",self.dept)
        print("Employee Salary:",self.sal)
class Manager(Employee):
    def accept_M(self):
        self.b=float(input("Enter Manager Bonus:"))
        print()
        self.t=self.sal+self.b
    def display_M(self):
        print("Manager Bonus:",self.b)
        print("Total Salary:",self.t)
ob=[]
n=int(input("Enter How may Managers:"))
print()
for i in range(0,n):
    obj=Manager()
    obj.accept_Emp()
    obj.accept_M()
    ob.append(obj)
max=ob[0].t
index=0
for i in range(1,n):
    if(max<ob[i].t):
        max=ob[i].t
        index=i
ob[index].display_Emp()
ob[index].display_M()
