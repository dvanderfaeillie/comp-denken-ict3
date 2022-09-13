#!/usr/bin/python
# -*- coding: utf-8 -*-
def discriminant( p, q ):
    D = -4 * p ** 3 -27 * q ** 2
    if D > 0 :
        print( 'Er zijn drie verschillende reële oplossingen' )
    elif D < 0:
        print( 'Er is exact één reële oplossing' )
    else:
        print( 'Van de drie oplossingen zijn er minstens twee aan elkaar gelijk' )
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()