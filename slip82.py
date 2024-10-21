class Demo:
    def get_String(self):
        self.s1=input("Enter any String:")
    def print_String(self):
        s=self.s1
        print("String in upper case:",(self.s1).upper())
        words=s.split(" ")
        print("String reversed word by word:",end=" ")
        for w in words:
            print(w[::-1].lower(),end=" ")
ob=Demo()
ob.get_String()
ob.print_String()
