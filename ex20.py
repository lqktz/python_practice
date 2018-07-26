# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(file_name):
    print file_name.read()

def rewind(file_name):
# seek 设置偏移byte数
    file_name.seek(0)

def print_a_line(line_count,file_name):
# readline()读取一行,直到\n,返回的是该行的值,包括\n,所以会有换行
# file 会记录每次readline读取后的位置,用于下次的读取
    print line_count,file_name.readline()

current_file = open(input_file)

print "Print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

'''
current_line和读取的行数没有半点关系,
之所以能一行行往下读取的原因是由于readline()方法
'''
