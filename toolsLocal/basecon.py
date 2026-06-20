#!/bin/env python

import sys
import argparse

### read ###
argparser = argparse.ArgumentParser(prog='BaseCon',
	description='Convert integer numbers of one numeric systems into up to 36 others.')
argparser.add_argument('input_system', type=int) #int1-36
argparser.add_argument('input_number', type=int)
argparser.add_argument('output_system',type=int) #int1-36
argparser.add_argument('-v', '--verbose', action='store_true', help='prints steps between calculations')
args = argparser.parse_args()
input_system = args.input_system
input_number = args.input_number 
output_system = args.output_system

### functions ###

def verbosity(*echo):
    if args.verbose:
        print(*echo)

def ziffernmenge(basis):
    if basis <= 10:
        return [str(i) for i in range(basis)]
    elif basis <= 36:
        # Verwende Buchstaben für Stellen größer als 9
        ziffern = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(basis - 10)]
        return ziffern
    else:
        raise ValueError("Basis zu groß – max. 36 unterstützt.")

### input recap ###

verbosity(input_system, input_number, output_system)
        
### main ###
stelle = ziffernmenge(output_system)
stellenwerte = len(stelle)

b = input_number
i = 0

while b >= 1:
	b = b/stellenwerte
	i += 1
verbosity("Stellen:", int(i))

conversed = ""
d = input_number
w = input_number

while i > 0:
	i = i-1
	zahl = d/(output_system**i)
	verbosity("Divisor: ", int(zahl))
	modulus = d%(output_system**i)
	verbosity("Modulo:", int(modulus))
	m = int((d-modulus)/(output_system**i))
	d = modulus
	verbosity("Übernahme nächste Stelle: ", int(m), int(d))
	conversed += stelle[m]
	
	
print("Dezimal ", input_number, " ist im Stellenwertsystem mit der Basis ", output_system, " ", conversed)
