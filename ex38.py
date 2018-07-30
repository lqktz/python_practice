# -*- coding: utf-8 -*-

ten_things = "apples oranges crows telephone light sugar"
print "wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ",stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print "111111".join(stuff)

#print stuff.join("222222")  error!!!!
print "stuff: ", stuff
print "#".join(stuff[3:5])
