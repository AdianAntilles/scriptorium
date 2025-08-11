#!/bin/env python

import sys

### read ###
decimal = int(sys.argv[1])
base = int(sys.argv[2])

### functions ###

def ziffernmenge(basis):
    if basis <= 10:
        return [str(i) for i in range(basis)]
    elif basis <= 36:
        # Verwende Buchstaben für Stellen größer als 9
        ziffern = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(basis - 10)]
        return ziffern
    else:
        raise ValueError("Basis zu groß – max. 36 unterstützt.")


        
### main ###
stelle = ziffernmenge(base)
stellenwerte = len(stelle)

b = decimal
i = 0
conversed = ""

while b >= 1:
	b = b/stellenwerte
	i += 1
#print("Stellen:", i)

d = decimal
w = decimal

while i > 0:
	i = i-1
	zahl = d/(base**i)
	#print("Divisor: ", int(zahl))
	modulus = d%(base**i)
	#print("Modulo:", modulus)
	m = int((d-modulus)/(base**i))
	d = modulus
	#print("Übernahme nächste Stelle: ", m, d)
	conversed += stelle[m]
	
	
print("Dezimal ", decimal, " ist im Stellenwertsystem mit der Basis ", base, " ", conversed)
