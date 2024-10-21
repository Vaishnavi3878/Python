class Negative_Integer(RuntimeError):
    def __init__(self,msg):
        self.msg=msg
try:
    n=int(input("Enter Number:"))
    if n<=0:
        raise Negative_Integer("Incorrect Input Number")
    print("Correct Input Number")
except Negative_Integer as e:
    print("Error:",e)
