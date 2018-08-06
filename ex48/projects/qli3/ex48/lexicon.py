# -*- coding: utf-8 -*-

class Lexicon(object):
    
    def __init__(self):
        self.directions = ('south','north','west','east','center')
        self.verbs = ('go','kill','eat','run','tell','shoot','sing','love')
        self.stops = ('the','in','of','to','via')
        self.nouns = ('bear','princess','door','tiger','cabinet')
 
        self.C_NUMBER = 'number'
        self.C_DIRECTION = 'direction'
        self.C_VERB = 'verb'
        self.C_STOP = 'stop'
        self.C_NOUNS = 'noun'
        self.C_ERROR = 'error'

    def scan(self,sentence):
        words = sentence.split(' ')
        my_list = []
        my_tuple = None

        for word in words:
            if None != self.isNumber(word):
                my_tuple = (self.C_NUMBER,self.isNumber(word))
                print "is a number"
            elif word in self.directions:
                my_tuple = (self.C_DIRECTION,word)
                print "direction ex48"
            elif word in self.verbs:
                my_tuple = (self.C_VERB,word)
                print "verb"
            elif word in self.stops:
                my_tuple = (self.C_STOP,word)
                print "stop"
            elif word in self.nouns:
                my_tuple = (self.C_NOUNS,word)
                print "nouns"
            else:
                my_tuple = (self.C_ERROR,word)
                print "ERROR"
            my_list.append(my_tuple)
        return my_list

    def isNumber(self,number):
        try:
            return int(number)
        except ValueError:
            return None

lexicon = Lexicon()
# lexicon.scan('123 bear of fo go')
