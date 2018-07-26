# -*- coding; utf-8 -*-
from sys import argv

script, name, age = argv
propt = ":"

print "Hi %s, I'm the %s script." % (name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s? " % name
likes = raw_input(propt)

print "Where do you live %s?" % name
lives = raw_input(propt)

print "What kind of computer do you have?"
computer = raw_input(propt)

print '''
Alright, so you said %r about liking me.
Your %r years old.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, age, lives, computer)

