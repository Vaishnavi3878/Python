class Demo:
    def accept(self):
        self.s1=input("Enter any String:")
    def reverse(self):
        s=self.s1
        words=s.split(" ")
        print("Original String:",s)
        print("Reverse String Word by Word:",end=" ")
        for w in words:
            print(w[::-1],end=" ")
ob=Demo()
ob.accept()
ob.reverse()
            
