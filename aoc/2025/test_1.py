#!/bin/env python

import math


dial = 50
nulls = 0
turns = []
#errer = False

with open("input_1.txt") as f:
    for line in f:
        cache = [line[0], int(line[1:].strip())]
        turns.append(cache)

def dance(start, direction, measure):
    if direction == "L":
        return (start - measure)
    elif direction == "R":
        return (start + measure)

for turn in turns:
    point = dial
    end = dance(point, turn[0], turn[1])
    if turn[0] == "L":
        for n in range(turn[1]):
            dial -= 1
            if dial < 0:
                dial = dial % 100
            if dial == 0:
                nulls += 1
    elif turn[0] == "R":
        for n in range(turn[1]):
            dial += 1
            if dial >= 100:
                dial = dial % 100
            if dial == 0:
                nulls += 1

    dial = end % 100

    print(dial, nulls)

print(nulls)
