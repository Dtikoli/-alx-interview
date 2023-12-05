#!/usr/bin/python3
""" Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists """


def canUnlockAll(boxes):
    """ Determines if boxes can be unlocked """
    if not boxes[0]:
        return False

    unlocked = {0}

    for index, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != index:
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False
