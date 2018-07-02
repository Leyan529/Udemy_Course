class Parent:
    n = 10
    def __init__(self):
        print("Parent Initialized")
    def parentFunc(self):
        print("Parent Func called")
    def setN(self, input):
        Parent.n = input
    def showN(self):
        print(str(Parent.n))

class Child(Parent):
    def __init__(self):
        print ("Child class initialized")
    def childFunc(self):
        print("Child being called")
    def showN(self):
        print(str(Parent.n + 10))

c = Child()
c.childFunc()
c.parentFunc()
c.setN(20)
c.showN()
# c.showChildN()