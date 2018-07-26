# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

#打开文件
#txt = open("ex15_sample.txt")
txt = open(filename)

print "Here's your file %r:" % filename

#打印出文件的内容,read返回是一个string
print txt.read()
txt.close()

print "%s, %s " % (script, filename)

'''
# 用于打开第二个文件
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
'''



