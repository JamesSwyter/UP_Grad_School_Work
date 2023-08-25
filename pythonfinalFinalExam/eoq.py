import math
import numbers

def eoq(D, A, v, r, include_costs=False):

    arglist = [D, A, v, r]

    if D <= 0 or A <= 0 or v <= 0 or r <= 0:
        print('1')

    if D <= 0 and A <= 0 and v <= 0 and r <= 0:
        print('2')

    if any([D <= 0, A <= 0, v <= 0, r <= 0]):
        print('3')

    #if all(arglist > 0):
     #   print('4')

    if any([x <= 0 for x in arglist]):
        print('5')

eoq(1,1,1,1)
print('                    ')
eoq(1,0,1,1)
print('                    ')
eoq(0,0,0,0)
print('                    ')
eoq(0,0,0,-1)
print('                    ')
eoq(1,-1,1,-1)

