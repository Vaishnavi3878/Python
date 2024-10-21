class Demo:
    def get_String(self):
        self.s1=input("Enter any String:")
    def print_String(self):
        print("String in upper case:",(self.s1).upper())
ob=Demo()
ob.get_String()
ob.print_String()
