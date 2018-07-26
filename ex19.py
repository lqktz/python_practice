# -*- coding: utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can user veriables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 30 + 5)

print "And we can combine the two, veriables and math:"
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 30)

'''
主要是使用函数调用,并没有什么特别注意的,python函数调用传参数可以有多种形式,
和其他的语言也没有太大的差别
python:参数对类型没有限制,至少在函数参数定义这一 步
'''
