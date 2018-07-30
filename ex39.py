# -*- coding: utf-8 -*-
states = {
        'Oregon': "OR",
        'Florida': 'FL',
        'Calofornia': 'CA',
        'new York': 'NY',
        'Michigan': 'MI'
        }

cities = {
        'CA': 'san franciso',
        'MI': 'detroit',
        "FL": 'jacksonville'
        }

cities['NY'] = "new York"
cities['OR'] = "Oregon"
"""
print '-' * 10
print "NY state has: ",cities['NY']
print "OR state has; ",cities["OR"]

print '-' * 10
print "Michigan has: ",cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]
"""
print states

print '-' * 10
for state,abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)


"""
print '-' * 10
for abbrev, city in cities.items():
    print "%s state is abbreviated %s and has city %s" % (
            state, abbrev, cities[abbrev])

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
            state, abbrev, cities[abbrev])

print '-' * 10
state = states.get("Texas",None)

if not state:
    print "sorry, no exist"

city = cities.get("TX", "does not exist")
print "The city for the state 'TX' is: %s" % city
"""
