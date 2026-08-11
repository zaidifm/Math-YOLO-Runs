#!/usr/bin/env python3
"""Exact low-degree certificates for the minimal scalar surjectivity phase diagram."""
import sympy as sp

t,k=sp.symbols('t k')

# m=4: exact square quartic for every k.
C=3+k
A=C/2
B=C*(1-k)/8
p4=sp.expand(C*B-1)
q4=sp.expand(B**2)
P4=sp.expand(t*(1+t)**3+k*t**2*(1+t)+p4*t+q4)
assert sp.expand(P4-(t**2+A*t+B)**2)==0

# m=3: exact triple-root cubic for every k != -1.
r=sp.simplify(-(2+k)/(3*(1+k)))
lead=1+k
p3=sp.simplify(3*lead*r**2-1)
q3=sp.simplify(-lead*r**3)
P3=sp.expand(t*(1+t)**2+k*t**2*(1+t)+p3*t+q3)
assert sp.factor(P3-lead*(t-r)**3)==0

print('m=4: for every k, an exact squareful quartic exists: VERIFIED')
print('  A=(3+k)/2, B=(3+k)(1-k)/8')
print('m=3: for every k!=-1, an exact triple-root cubic exists: VERIFIED')
print('Therefore every nonzero scalar m=3 and m=4 map is nonsurjective.')
