#!/usr/bin/python3
'''module for the lockbox method'''


def canUnlockAll(boxes):
    '''This function determines if all the boxes can be unlocked'''

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
