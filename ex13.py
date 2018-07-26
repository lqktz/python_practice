# -*- coding: utf-8 -*-
'''
from sys import argv


script, first, second, third = argv

print "The script is called:", script
print "Your first variable is :", first
print "Your second variable is :", second
print "Your third variable is :",third

something = raw_input("input something: ")
print something
'''


'''
可以对比以上两种输入方式
'''

# 这是使用import sys 与 from sys import argv 方式进行对比
# 可以参考: https://blog.csdn.net/weixin_41321234/article/details/79099233
import sys

#script, first, second, third = argv
script = sys.argv[0]
first = sys.argv[1]
second = sys.argv[2]
third = sys.argv[3]


print "The script is called:", script
print "Your first variable is :", first
print "Your second variable is :", second
print "Your third variable is :",third
