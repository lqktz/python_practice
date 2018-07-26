# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

srcipt, from_file, out_file = argv

print "Copying from %s to %s." % (from_file, out_file)

in_file = open(from_file)
indata = in_file.read()
'''
indata = open(from_file).read()
这样就不用使用close关闭文件
'''
print "The file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(out_file)
print "Ready, hit RETURN to continue,CTRL-C to abort."

raw_input()

out_file_obj = open(out_file,'w')
out_file_obj.write(indata)

print "Alright, all done."

in_file.close()
out_file_obj.close()
