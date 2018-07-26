# -*- coding: utf-8 -*-
def add(a, b):
    print "add: %d + %d " % (a, b)
    return a + b

def subtract(a, b):
    print "sub: %d -%d " % (a, b)
    return a - b

def multiply(a, b):
    print "mul: %d * %d" % (a, b)
    return a * b

def devide(a, b):
    print "devide %d / %d" % (a, b)
    return a / b

print "Let't do some math with just function!"

age = add(20, 8)
height = subtract(178, 1)
weight = multiply(90, 2)
iq = devide(100,2)

print "Age: %d, height: %d, weight: %d,iq: %d" % (age, height, weight, iq)

print "Herr is a puzzle!!!"

what = add(age, subtract(height,multiply(weight, devide(iq, 2))))

print "That become: ",what, "Can you do it by hand?"
