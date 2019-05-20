class B:
    def __init__(self):
        pass
   
    def setA(self,a):
        self.a = a

    def BcallA(self):
        self.a.call()

    def run(self):
        print("branch devb conflict")
        print("This is class B")
