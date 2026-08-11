#!/usr/bin/env python3
"""Exact bridge between the BLIND4 binary-cubic frame and the boundary SL2 frame."""
import sympy as sp

x,y,z,X,W = sp.symbols('x y z X W')
u = 1 + x*y
v = 1 + 2*x*y
p = 3*y + x*z
L = -1 + 3*x*y + x**2*z
K = y + 6*x*y**2 + x*z + 2*x**2*y*z

J1 = sp.Matrix([[1,x],[y,u]])
J2 = sp.Matrix([[1,x],[2*y,v]])
w = sp.Matrix([[0,1],[-1,0]])
nminus_p = sp.Matrix([[1,0],[p,1]])
G = sp.Matrix([[x,v],[L,K]])

assert sp.expand(J1.det()) == 1
assert sp.expand(J2.det()) == 1
assert sp.simplify(nminus_p * J2.inv() * w - G) == sp.zeros(2)
assert sp.expand(L - (x*p-1)) == 0
assert sp.expand(K - (v*p-2*y)) == 0

alpha = (3*u-1)*z + 9*y**2
beta = 3*x*u*z + 3*y*(3*u-2)
assert sp.expand(beta - 3*(u*p-2*y)) == 0
assert sp.expand(x*alpha - (beta-p)) == 0

ell, m = J1.inv() * sp.Matrix([X,W])
P = sp.expand(ell*(2*m**2 + beta*ell*m + alpha*ell**2))
F1 = sp.expand(u**3*z + y**2*u*(4+3*x*y))
F2 = sp.expand(y + 3*x*u**2*z + 3*x*y**2*(4+3*x*y))
F3 = sp.expand(2*x - 3*x**2*y - x**3*z)
Ptarget = sp.expand(2*F1*X**3 - F2*X**2*W + 2*X*W**2 - F3*W**3)

assert sp.expand(P-Ptarget) == 0
assert sp.expand(sp.diff(P,X).subs({X:x,W:u}) - 2*u) == 0
assert sp.expand(sp.diff(P,W).subs({X:x,W:u}) + 2*x) == 0
assert sp.expand(F3 - x*(1-L)) == 0

print('det J1 = det J2 = 1: VERIFIED')
print('boundary G = n_-(p) J2^-1 w: VERIFIED')
print('L=xp-1 and K=vp-2y: VERIFIED')
print('beta=3(up-2y) and x alpha=beta-p: VERIFIED')
print('binary cubic expands to exact F1,F2,F3 coefficients: VERIFIED')
print('normalized gradient at (x,u) is 2(u,-x): VERIFIED')
print('F3=x(1-L): VERIFIED')
