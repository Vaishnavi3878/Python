class Student:
    def accept(self):
        self.name=input("Enter Student name:")
        self.mark=int(input("Enter Student marks:"))
    def modify(self):
        self.oldmark=self.mark
        self.mark=int(input("Enter student modified marks:"))
        print("Student Name:",self.name)
        print("Student Old Marks:",self.oldmark)
        print("Student Modified Marks:",self.mark)
ob=Student()
ob.accept()
ob.modify()
