class ClassName:
    pass

class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def out(self):
        print(self.name)
        print(self.age)
        print(self.grade)
    def display(self):
        return ("Student name is " + self.name)

S1 = Students("Bob",12,"6th")
S1.out()
print (S1.display())

S2=Students("Abby",7,"13th")
print (hasattr(S2,"age"))  #hasattr(object , attr ) 檢驗是否存在屬性
print (hasattr(S2,"gr"))

setattr(S1,"love","Abby") #setattr(object , new attr , value) 事後增加屬性
print (hasattr(S1,"love"))

print (getattr(S1,"name")) #getattr (object , attr )同jave get
print (getattr(S2,"name"))
print (getattr(S1,"love"))

delattr(S1,"love") #delattr(object , attr) 事後刪除屬性
print(hasattr(S1,"love"))