# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "If you don't want that,hit ctrl-c."
print "if you do want that, hit return."

raw_input("?")

print "Opening the file ..."
'''
打开方式有w r a,分别是对应写,读,追加
write read append
还有 w+ a+ r+控制符来控制文件访问
open(filename)是默认用r权限打开的
'''
target = open(filename,'a')

print "Truncating the file. Goodbye!"
# open()函数用w权限打开,不需要用该方法清理
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

# 习题3
formatter = "%s\n%s\n%s\n"
target.write(formatter % (line1, line2, line3))

print "And finally, we close it."
target.close()

#读取写入的文件
txt = open(filename)
print txt.read()
txt.close()
