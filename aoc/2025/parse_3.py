#!/bin/env python3

with open("input_3.txt") as f:
    #for i in f.read():
    struct = [ y for y in f.read().split() ]
#print(struct)

# return list of all indices with max value
def maximal(pant):
    laest = [ int(letter) for letter in pant]
    maxi = max(laest)
    indiziert = [ i for i, x in enumerate(laest) if x == maxi ]
    return indiziert

count = 0
for element in struct:
    candies = maximal(element)
    print(element, candies)
    if candies[0] == '99':
        valie = str(max(element[:-1])) + str(element[99])
        print(valie)
    elif len(candies) == 1:
        valie = str(max(element[candies[0]])) + str(max(element[int(candies[0])+1:]))
        print(valie)
    else:
        valie = 2 * str(element[int(candies[0])])
        print(valie)

"""

candid = []
    for strinx in candies:
        #   print(strinx)
        #lists = [ int(letter) for letter in str(strinx) ]
        candid.append(element[strinx:])
       # print(candid)
    for cane in candid:
        # print("Sugar: " + cane)
        uni = maximal(cane) #list 
        neo = max(uni)
        if len(cane) > 1:
            #    print(uni, neo)
            valie = str(cane[0]) + str(max(cane[1:]))
        elif len(cane) == 1:
            #   print("Größter Wert ist letzter Wert." + cane)
           # print(uni, neo, str(uni), str(neo))
            valie = str(max(element[:-1])) + str(cane[-1])
           # print(valie)
    #print(valie)
    count = count + int(valie)
"""
print(count)
