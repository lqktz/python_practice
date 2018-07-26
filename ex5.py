# -*- coding: utf-8 -*-

my_name = "qli3"
my_age = 28

print "Let's talk about %s." % my_name
print "My name is %s,my age is %s." % (my_name, my_age)

a = 3
b = 4

print " %d + %d = %d ."% (a, b, a + b)

# %r
x = 3
y = "30 string"

print "%r ,%r "% (x, y)

# 美元 和 人民币 之间的转换
money = 13
print "%d dollar is %.2f RMB. "% (money, money * 5.8)

# 四舍五入
x = 2.4
y = 2.5

print "x = %f,y = %f, x = %f,y = %f" % (x,y,round(x),round(y))
