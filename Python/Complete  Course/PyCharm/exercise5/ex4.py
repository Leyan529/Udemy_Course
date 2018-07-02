class ball:
    def __init__(self,name):
        self.name = name
    def hello(self):
        s = "Hello %s "
        print(s%(self.name))

b = ball("bobo")
b.hello()

