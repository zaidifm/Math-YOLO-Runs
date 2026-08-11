#!/usr/bin/env python3
"""Exact verification for the scalar degree-17 canonical family."""
import sympy as sp

x,y,z,lam = sp.symbols('x y z lambda')
a,W = sp.symbols('a W')
t,r,s,k = sp.symbols('t r s k')
St,Ut,wt = sp.symbols('S U w')

v=1+2*x*y
L=-1+3*x*y+x**2*z
K=y+6*x*y**2+x*z+2*x**2*y*z
Wsrc=sp.expand(x*L)
R=sp.expand(v*L)
S0=sp.expand(8*x**3*y**3*z+24*x**2*y**4+12*x**2*y**2*z+28*x*y**3+6*x*y*z+8*y**2+z)
U0=sp.expand(12*x**3*y**2*z+36*x**2*y**3+12*x**2*y*z+24*x*y**2+3*x*z+y)

dS=sp.expand(lam*sp.Rational(1,2)*v**2*K**2*(1+4*R))
dU=sp.expand(2*lam*x**2*v*K**3+3*lam*x*L*v**2*K**2)
Smap=sp.expand(S0+dS); Umap=sp.expand(U0+dU)

# Hidden differentiation cross-check.
aexpr=v/x
h0=a**2+W*a**3
g=lam*a**2*(1+a*W)**3
assert sp.cancel(sp.diff(g,a).subs({a:aexpr,W:Wsrc})-dU)==0
Ng=sp.expand(a*sp.diff(g,a)-g)
assert sp.cancel((Ng/2).subs({a:aexpr,W:Wsrc})-dS)==0

# Keller determinant and degrees.
J=sp.Matrix([[sp.diff(Smap,q) for q in (x,y,z)],
             [sp.diff(Umap,q) for q in (x,y,z)],
             [sp.diff(Wsrc,q) for q in (x,y,z)]])
assert sp.factor(J.det())==1
assert sp.Poly(Smap,x,y,z).total_degree()==17
assert sp.Poly(Umap,x,y,z).total_degree()==16
assert sp.Poly(Wsrc,x,y,z).total_degree()==4

# Boundary coverage.
assert sp.expand(Wsrc.subs(x,0))==0
assert sp.expand(Umap.subs(x,0)-y)==0
assert sp.expand(Smap.subs(x,0)-(z+sp.Rational(1,2)*(16-3*lam)*y**2))==0

# Recovery quintic.
h=sp.expand(h0+g)
P=sp.expand(lam*t**5+3*lam*t**4+(1+3*lam)*t**3+(1+lam)*t**2-Ut*wt*t+2*St*wt**2)
Pdirect=sp.factor(wt**2*(h.subs({a:t/wt,W:wt})-Ut*t/wt+2*St))
assert sp.expand(P-Pdirect)==0

# Squareful elimination.
s_expr=-sp.Rational(3,2)*(1+r)
E2=sp.expand(4*k+15*r**2+18*r+3)
E3=sp.expand(4*k-5*r**3+18*r**2+27*r+4)
res=sp.factor(sp.resultant(E2,E3,r))
assert sp.expand(res-320*k*(5*k**2+99*k+27))==0
Qk=sp.expand(5*k**2+99*k+27)
Qlam=sp.expand(27*lam**2+99*lam+5)
assert sp.expand(lam**2*Qk.subs(k,1/lam)-Qlam)==0
roots=sp.solve(Qlam,lam)

# Explicit exceptional witnesses.
r0=-(2*k+3)/21
s0=(k-9)/7
U0bad=(3-4*k)/15
S0bad=-(28*k+9)/250
Pbad=sp.together(P.subs({lam:1/k,wt:1,Ut:U0bad,St:S0bad}))
Fbad=sp.together((1/k)*(t-r0)**3*(t-s0)**2)
num=sp.together(Pbad-Fbad).as_numer_denom()[0]
for cc in sp.Poly(sp.expand(num),t).all_coeffs():
    assert sp.rem(sp.Poly(sp.expand(cc),k),sp.Poly(Qk,k)).as_expr()==0

# Lambda=0 omitted curve.
P0=sp.expand(P.subs(lam,0))
P0bad=sp.expand(P0.subs({Ut:-1/(3*wt),St:1/(54*wt**2)}))
assert sp.expand(P0bad-(t+sp.Rational(1,3))**3)==0

print('symbolic Jacobian determinant det=1 for all lambda: VERIFIED')
print('generic lambda!=0 degree profile (S,U,W)=(17,16,4): VERIFIED')
print('boundary W=0 coverage: VERIFIED')
print('W!=0 quintic recovery polynomial: VERIFIED')
print('squareful elimination resultant: 320*k*(5*k^2+99*k+27): VERIFIED')
print('exceptional lambdas:', roots)
print('constructive omitted targets at both exceptional lambdas: VERIFIED')
print('lambda=0 omitted curve: VERIFIED')
