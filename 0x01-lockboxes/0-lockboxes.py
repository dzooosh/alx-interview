#!/usr/bin/python3
""" This is the Lockboxes where each box may contain
    keys to the other boxes
    A key with the same number as a box opens that box
"""


def canUnlockAll(boxes):
    """
    Arg:
        boxes - list of lists (from 0 to (n - 1))
    Return - True if all boxes can be opened
             else False
    """

    # boxes[0]
    # number of box in boxes
    # creating a set which contains unique numbers found in the accessed box
    box_list = []
    for box in range(len(boxes)):
        box_list.append(box)

    key_list = [0]
    for x in boxes[0]:
        if x == 0:
            continue
        key_list.append(x)

    for no in key_list:
        for key in boxes[no]:
            if key in key_list or key is None:
                continue
            else:
                key_list.append(key)

    # check if number is not in key_list - if it is don't bother to add
    # else add and loop through the box unlocked

    if sorted(key_list) == sorted(box_list):
        return True
    else:
        return False
