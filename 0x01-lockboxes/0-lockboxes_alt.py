#!/usr/bin/python3
""" Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists """


def canUnlockAll(boxes):
    """ Determines if boxes can be unlocked """
    unlocked = {}

    for index, box in enumerate(boxes):
        if len(box) == 0 or index == 0:
            unlocked[index] = index
        for key in box:
            if key < len(boxes) and key != index:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
    return False
