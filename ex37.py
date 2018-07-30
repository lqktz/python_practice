# -*- coding: utf-8 -*-
# 关键字

print """
and : 与
del : 用于删除变量
    a = 10
    del a
    b = [1, 2, 3, 4]
    del b[2]
    b就变为:[1, 2, 4]
or : 或
from : 导包,from ... import ...
not : 非
while : 循环
with ... as ... :
    with open("/tmp/foo.txt") as file:
        data = file.read()
pass :空语句,保证语句结构的完整性
if ... elif ... else ... : if 语句
assert :断言函数,断言是声明其布尔值必须为真的判定,为真就通过,为假就报错
break : 结束循环体,之后的代码不再执行
continue : 结束此次循环,进入到下一次循环
yield : 生成器
raise : 引发一个异常
try ...finally :finally语句在程序出错之前会被执行
    a=10
    b=0
    try:
        print a/b
    finally:
        print "always excute"

try...except :
    a=10
    b=0
    try:
        c=a/b
        print c
    except ZeroDivisionError,e:
        print e.message
有异常except才会被执行

print "-------------"
a=10
b=0
try:
    c = b/ a
    print c
except (IOError ,ZeroDivisionError),x:
    print x
else:
    print "no error"
    print "done"
没有异常else才会被执行

try ... except ... finally :
a=10
b=0
try:
    print a/b
except:
    print "error"
finally:
    print "always excute"

lambda : 匿名函数
is : 两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同
== :判断两个值是不是一样

"""


