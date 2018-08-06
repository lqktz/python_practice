# -*- coding: utf-8 -*-
class X():
    def __init__(self):
        self.a = 10

    def test1(self):
        print "X test1()"

class Y(X):
    def __init__(self):
        self.b = 20

    def test2(self):
        print "Y test2()"


x = X()
print x.a
y = Y()
print y.b
y.test1()
y.test2()
