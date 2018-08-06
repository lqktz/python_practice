# -*- coding: utf-8 -*-
import ex40_1

ex40_1.apple()

print ex40_1.a

class Myclazz(object):
    def __init__(self):
        self.aaa = "This is MyclaZZ self aaa"

    def apple(self):
        print "clazz apple"

myObject = Myclazz()
print myObject.aaa
myObject.apple()

