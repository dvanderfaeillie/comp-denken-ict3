#!/usr/bin/python
# -*- coding: utf-8 -*-

def zeef_eratosthenes( max: int ) -> list:
    lijst = list( range( 1, max + 1 ) )
    priemgetallen = []

    lijst[ 0 ] = 0 # 1 is not prime
    for getal in lijst:
        if getal != 0:
            priemgetallen.append(getal)
            for k in range( 2, max // getal + 1 ):
                lijst[ getal * k - 1 ] = 0  
    
    return priemgetallen
