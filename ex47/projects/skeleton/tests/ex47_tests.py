# -*- coding: utf-8 -*-

from nose.tools import *
from ex47.game import Room

def test_Room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grap,There's a 
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths,{})

def test_room_paths():
    center = Room("Center","Test room in the cneter.")
    north = Room("North","Test room in the north.")
    south = Room("South","Test room in the south.")

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are tres ,you can go east,")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west':west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

"""
run 'nosetests'
"""

