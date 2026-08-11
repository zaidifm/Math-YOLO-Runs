#!/usr/bin/env python3
"""Exact symbolic checks for the 2026-08-11 Jacobian blackboard synthesis.

This script verifies identities; the general proofs are in the companion Markdown note.
"""
import sympy as sp

x,y,z = sp.symbols('x y z')
A,Ws = sp.symbols('a W')
W,B,C,Q = sp.symbols('W B C Q')

v = 1 + 2*x*y
L = -1 + 3*x*y + x**2*z
K = y + 6*x*y**2 + x*z + 2*x**2*y*z
w = sp.expand(x*L)
b = sp.expand(x*K)
c = sp.expand(v*K)
q = sp.expand(2*b - 1)

# Fundamental SL2 identity and boundary ring identities.
assert sp.expand(x*K - v*L) == 1
assert sp.expand(1 + v*L - x*K) == 0
assert sp.expand(c*w - b*(b-1)) == 0
assert sp.expand(q**2 - 4*c*w) == 1

# Exact SL2 matrix factorization.
G = sp.Matrix([[x,v],[L,K]])
assert sp.expand(G.det()) == 1
Gfac = (sp.Matrix([[1,0],[3*y+x*z,1]])
        * sp.Matrix([[x,1],[-1,0]])
        * sp.Matrix([[1,2*y],[0,1]]))
assert sp.simplify(Gfac-G) == sp.zeros(2)

# On x != 0, torus-normalize first entry to 1.
# diag(1/x,x)*G = [[1,a],[W,b]] with a=v/x.
N = sp.diag(1/x,x)*G
assert sp.simplify(N[0,0]-1) == 0
assert sp.simplify(N[0,1]-v/x) == 0
assert sp.simplify(N[1,0]-w) == 0
assert sp.simplify(N[1,1]-b) == 0
assert sp.simplify(N.det()-1) == 0

# Product of row linear forms gives the discriminant-one quadratic.
u,t = sp.symbols('u t')
quad = sp.expand((x*u+v*t)*(L*u+K*t))
assert sp.expand(quad - (w*u**2 + q*u*t + c*t**2)) == 0

# sl2 derivations on R = k[W,Q,C]/(Q^2-4CW-1).
def deriv(expr, images):
    return sp.expand(sum(sp.diff(expr,g)*images[g] for g in (W,Q,C)))

e_img = {W:0, Q:2*W, C:Q}
f_img = {W:Q, Q:2*C, C:0}
h_img = {W:2*W, Q:0, C:-2*C}
rel = Q**2 - 4*C*W - 1
assert sp.expand(deriv(rel,e_img)) == 0
assert sp.expand(deriv(rel,f_img)) == 0
assert sp.expand(deriv(rel,h_img)) == 0
for g in (W,Q,C):
    ef = deriv(deriv(g,f_img),e_img) - deriv(deriv(g,e_img),f_img)
    assert sp.expand(ef - h_img[g]) == 0
    he = deriv(deriv(g,e_img),h_img) - deriv(deriv(g,h_img),e_img)
    assert sp.expand(he - 2*e_img[g]) == 0
    hf = deriv(deriv(g,f_img),h_img) - deriv(deriv(g,h_img),f_img)
    assert sp.expand(hf + 2*f_img[g]) == 0

# Leading homogeneous forms of W,b,c in original variables.
def top_hom(expr):
    P = sp.Poly(sp.expand(expr),x,y,z)
    d = P.total_degree()
    out = 0
    for mon,coef in P.terms():
        if sum(mon)==d:
            out += coef*x**mon[0]*y**mon[1]*z**mon[2]
    return d,sp.expand(out)

assert top_hom(w) == (4, x**3*z)
assert top_hom(b) == (5, 2*x**3*y*z)
assert top_hom(c) == (6, 4*x**3*y**2*z)
assert sp.expand(top_hom(b)[1]**2 - top_hom(w)[1]*top_hom(c)[1]) == 0

# Canonical minimal directions for recovery degree m.
# Return g in hidden a,W variables and expected output-degree threshold.
def min_direction(m):
    bb = 1 + A*Ws
    cc = A*bb
    if m % 2:  # m=2r+1
        r = (m-1)//2
        g = sp.expand(bb*cc**r)
        D = 3*m+2
    else:      # m=2r
        r = m//2
        g = sp.expand(bb**2*cc**(r-1))
        D = 3*m+4
    return g,D

for m in range(1,13):
    g,D = min_direction(m)
    assert sp.Poly(g,A,Ws).degree(A) == m
    # Pull back to original variables and check exact polynomialization.
    gp = sp.cancel(g.subs({A:v/x, Ws:w}))
    assert sp.denom(gp) == 1
    if m >= 2:
        assert sp.Poly(sp.expand(gp),x,y,z).total_degree() == D
    dU = sp.diff(g,A)
    dS2 = sp.expand(A*dU-g)
    Up = sp.cancel(dU.subs({A:v/x, Ws:w}))
    S2p = sp.cancel(dS2.subs({A:v/x, Ws:w}))
    assert sp.denom(Up) == 1 and sp.denom(S2p) == 1
    if m >= 2:
        assert max(sp.Poly(sp.expand(Up),x,y,z).total_degree(),
                   sp.Poly(sp.expand(S2p),x,y,z).total_degree()) == D

print('SL2 determinant/exchange identity: VERIFIED')
print('SL2 matrix factorization: VERIFIED')
print('Torus-normalized hidden big cell [[1,a],[W,1+aW]]: VERIFIED')
print('Discriminant-one quadratic q^2-4cW=1: VERIFIED')
print('sl2 derivation relations: VERIFIED')
print('Leading degree triple (W,b,c)=(4,5,6) and cone relation: VERIFIED')
print('Canonical minimal directions m=1..12: VERIFIED')
for m in range(3,13):
    _,D=min_direction(m)
    print(f'm={m}: predicted sharp deformation degree {D}')
