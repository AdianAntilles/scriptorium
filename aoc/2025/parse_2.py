#!/bin/env python3

id_lists = []
score = 0

for line in open('input_2.txt'):
    id_lists = line.strip().split(",") 
#Gepetto:
# with open("input_2.txt") as f:
#    id_lists = f.readline().strip().split(",")


def dividers(x):
    i = 1
    div_list = []
    while i <= x//2:
        if x%i == 0:
            div_list.append(i)
        i+=1
    return div_list

# def divisors(n):
#    return [i for i in range(1, n + 1) if n % i == 0]
# für große Listen
# import math
# def divisors(n):
#    res = []
#    for i in range(1, int(math.sqrt(n)) + 1):
#        if n % i == 0:
#            res.append(i)
#            if i != n // i:
#               res.append(n // i)
#    return sorted(res)

def chit(k):
    diva_list = dividers(len(k))
    for devi in diva_list:
        blocks = [k[i:i+devi] for i in range(0, len(k), devi)]
        if all(bb == blocks[0] for bb in blocks):
            #print(blocks)
            return True
    return False

###
#def has_repetition(s):
#    n = len(s)
#
#    for size in range(1, n//2 + 1):
#        if n % size == 0:
#            blocks = [s[i:i+size] for i in range(0, n, size)]
#            if len(set(blocks)) == 1:
#                return True
#
#    return False
####

for entry in id_lists:
    begins, ends = entry.split("-")
    begin = int(begins)
    end = int(ends)
    for number in range(begin, end):
        if chit(str(number)):
            score += number

print(score)
