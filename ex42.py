# -*- coding: utf-8 -*-
class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

dog = Dog("little dog")
print dog.name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
    #  调用父类的构造方法,进行初始化
        super(Employee, self).__init__(name)
        self.salary = salary

employee = Employee("qli3",100)

print employee.name, employee.salary

"""
附件练习5:
>>> dic = {}
>>> key = 1
>>> val1 = 2
>>> val2 = 3
>>> val3 = 4
>>> dic.setdefault(key,[]).append(val1)
>>> print dic
{1: [2]}
>>> dic.setdefault(key,[]).append(val2)
>>> dic.setdefault(key,[]).append(val3)
>>> print dic
{1: [2, 3, 4]}
>>> print dic[key]
[2, 3, 4]
>>> print list(dic[key])
[2, 3, 4]
"""
