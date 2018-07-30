# -*- coding: utf-8 -*-
print "you enter a dark root with  two doors, Do you go through door #1 or door #2?"

door = raw_input(">")

if door =="1":
    print "There's a giant bear here eating a cheese cake. what do you do ?"
    print "1. take the cake."
    print "2. scream at the bear."

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs aways. " % bear
elif door == "2":
    print "You stare into  the endless abyss at cthulhu's retina."
    print "1. BlueBerries."
    print "2. yellow jacket clothespins."
    print "3. understanding revolvers yelling melodies."

    instanity = raw_input(">")

    if instanity == "1" or instanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"

