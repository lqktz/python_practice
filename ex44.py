# -*- coding: utf-8 -*-
class Parent(object):

    def __init__(self,name):
        self.name = name

    def func1(self):
        print "Parent func1"

    def func2(self):
        print "Parent func2"

    def func3(self):
        print "Parent func3"

class Child(Parent):
    def func2(self):
        print "Child func2"

    def func3(self):
        print "Child func3 start"
        super(Child,self).func3()
        print "Child func3 end"

    def func4(self):
        print "func4"
        super(Child,self).func3()

class B(object):

    def __init__(self):
        pass
    def func(self):
        print "B B B"

class A(object):

    def __init__(self):
        self.other = B()

    def func(self):
        self.other.func()


# 继承
dad = Parent("qli3")
son = Child("child")

dad.func1()
son.func1()

dad.func2()
son.func2()

dad.func3()
son.func3()

son.func4()

# 合成
b = B()
b.func()

a = A()
a.func()
