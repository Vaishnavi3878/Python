class complex1:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def __add__(self,ob1):
        real_sum=self.real + ob1.real
        img_sum=self.img + ob1.img
        print("Sum :",real_sum,"+",img_sum,"i")
        
ob=complex1(10,20)
ob1=complex1(100,200)
ob+ob1
