class Student:
    address = '青岛'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('name:',self.name,'age:',self.age)

stu = Student('崔涛','01')
print(stu.name)
print(stu.age)


