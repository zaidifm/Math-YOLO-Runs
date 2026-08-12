#!/usr/bin/env python3
import sympy as sp

x,y,z=sp.symbols('x y z')
alpha,beta,p,q,gamma=sp.symbols('alpha beta p q gamma')

a=1/x + alpha*y + beta*z
W=-x**2 + x**3*(p*y+q*z)
Delta=alpha*q-beta*p

Jsrc=sp.Matrix([
    [sp.diff(1/x,v) for v in (x,y,z)],
    [sp.diff(a,v) for v in (x,y,z)],
    [sp.diff(W,v) for v in (x,y,z)],
]).det()
assert sp.expand(Jsrc + Delta*x)==0

b=sp.expand(1+a**2*W)
K=sp.cancel(b/x)
assert sp.denom(K)==1
c=sp.cancel(a*b)
assert sp.denom(c)==1
c0=sp.expand(sp.limit(c,x,0))
assert sp.expand(c0-((p-2*alpha)*y+(q-2*beta)*z))==0

ah,Wh=sp.symbols('ah Wh')
bh=1+ah**2*Wh
h=sp.Rational(1,2)*ah**2*bh + gamma*ah**2*bh**2
ha=sp.diff(h,ah)
U=sp.cancel(1/x + ha.subs({ah:a,Wh:W}))
hsub=sp.cancel(h.subs({ah:a,Wh:W}))
S=sp.cancel((a*U-hsub)/Delta)
assert sp.denom(U)==1
res=sp.factor(sp.limit(x*S,x,0))
expected=((8-16*gamma)*(alpha*y+beta*z)+(8*gamma-3)*(p*y+q*z))/(2*(-Delta))
assert sp.simplify(res-expected)==0

rho_y=3*p-8*alpha
rho_z=3*q-8*beta
c0_y=p-2*alpha
c0_z=q-2*beta
wedge=sp.expand(rho_y*c0_z-rho_z*c0_y)
assert sp.expand(wedge + 2*Delta)==0

rhog_y=(3-8*gamma)*p + (-8+16*gamma)*alpha
rhog_z=(3-8*gamma)*q + (-8+16*gamma)*beta
wedge_g=sp.expand(rhog_y*c0_z-rhog_z*c0_y)
assert sp.expand(wedge_g + 2*Delta)==0

print('k=2 source Jacobian = -Delta*x: VERIFIED')
print('b=1+a^2 W divisible by x and c=a b polynomial: VERIFIED')
print('boundary coordinate c0 = s-2r: VERIFIED')
print('incidence residue formula through all residue-relevant d=2 corrections: VERIFIED')
print('residue wedge c0 = -2 Delta, independent of gamma: VERIFIED')
print('therefore nonzero source Jacobian (Delta != 0) is incompatible with residue being a boundary function: VERIFIED')
