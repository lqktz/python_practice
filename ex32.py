# -*- coding: utf-8 -*-
the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first king of for-loop throught a list
for number  in the_count:
    print "This is  count %d" % number

# same as above
for fruit in fruits:
    print "This is fruit %s." % fruit

# also we can go throught mixed lists too
# notice we have to use %r since wo don't know what's in it.
for i in change:
    print "I got %r in change." % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0~5 counts.
for i in range(0, 6):
    print "Adding %d to the list. " % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "element was : %d" % i

"""
 重点:
 1. 使用for遍历list
 2. 了解list的方法
"""
