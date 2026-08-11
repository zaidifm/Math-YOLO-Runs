#!/usr/bin/env python3
"""Exact low-degree certificates for the minimal-direction surjectivity theorem."""
import sympy as sp

t,k=sp.symbols('t k')

def coeff(poly,deg):
    return sp.Poly(sp.expand(poly),t).coeff_monomial(t**deg)

# m=6: square cubic.
A,B,C=sp.symbols('A B C')
Q3=t**3+A*t**2+B*t+C
sq6=sp.expand(Q3**2)
assert sp.solve(sp.Eq(coeff(sq6,5),4),A)[0]==2
sq6a=sp.expand(sq6.subs(A,2))
assert sp.solve(sp.Eq(coeff(sq6a,4),6),B)[0]==1
sq6b=sp.expand(sq6a.subs(B,1))
assert sp.solve(sp.Eq(coeff(sq6b,3),4+k),C)[0]==k/2
assert sp.expand(coeff(sq6b.subs(C,k/2),2)-(1+k))==k

# m=6: cube quadratic.
A,B=sp.symbols('A B')
Q2=t**2+A*t+B
cu6=sp.expand(Q2**3)
assert sp.solve(sp.Eq(coeff(cu6,5),4),A)[0]==sp.Rational(4,3)
cu6a=sp.expand(cu6.subs(A,sp.Rational(4,3)))
assert sp.solve(sp.Eq(coeff(cu6a,4),6),B)[0]==sp.Rational(2,9)
cu6b=sp.expand(cu6a.subs(B,sp.Rational(2,9)))
k6=sp.expand(coeff(cu6b,3)-4)
assert k6==sp.Rational(4,27)
assert sp.expand(coeff(cu6b,2)-(1+k6))==sp.Rational(5,27)

# m=7: quadratic^2 * linear^3.
a,b,c=sp.symbols('a b c')
fac7=sp.expand((t**2+a*t+b)**2*(t+c)**3)
aexpr=(4-3*c)/2
bexpr=(15*c**2-24*c+8)/8
assert sp.expand(coeff(fac7.subs({a:aexpr,b:bexpr}),6)-4)==0
assert sp.expand(coeff(fac7.subs({a:aexpr,b:bexpr}),5)-6)==0
eq4=sp.factor(8*(coeff(fac7.subs({a:aexpr,b:bexpr}),4)-4))
assert eq4==c*(35*c**2-60*c+24)
kexpr=sp.expand(coeff(fac7.subs({a:aexpr,b:bexpr}),3)-1)
compat=sp.factor(64*(coeff(fac7.subs({a:aexpr,b:bexpr}),2)-kexpr))
assert compat==-c*(21*c**4-135*c**3+448*c**2-528*c+192)
q7=35*c**2-60*c+24
q7b=21*c**4-135*c**3+448*c**2-528*c+192
assert sp.resultant(q7,q7b,c)==24869376
assert sp.expand(kexpr.subs(c,0))==0

# m=8: square quartic.
a1,a2,a3,a4=sp.symbols('a1 a2 a3 a4')
Q4=t**4+a1*t**3+a2*t**2+a3*t+a4
sq8=sp.expand(Q4**2)
sol={a1:sp.Rational(5,2)}
sol[a2]=sp.solve(sp.Eq(coeff(sq8.subs(sol),6),10),a2)[0]
sol[a3]=sp.solve(sp.Eq(coeff(sq8.subs(sol),5),10),a3)[0]
sol[a4]=sp.solve(sp.Eq(coeff(sq8.subs(sol),4),5),a4)[0]
assert sol[a2]==sp.Rational(15,8)
assert sol[a3]==sp.Rational(5,16)
assert sol[a4]==-sp.Rational(5,128)
sq8f=sp.expand(sq8.subs(sol))
k8=sp.expand(coeff(sq8f,3)-1)
assert k8==-sp.Rational(3,128)
assert sp.expand(coeff(sq8f,2)-k8)==-sp.Rational(13,512)

# m=8: linear^2 * quadratic^3.
a,b,c=sp.symbols('a b c')
fac8=sp.expand((t+a)**2*(t**2+b*t+c)**3)
top=[sp.expand(coeff(fac8,7)-5),sp.expand(coeff(fac8,6)-10),
     sp.expand(coeff(fac8,5)-10),sp.expand(coeff(fac8,4)-5)]
GB=sp.groebner(top,a,b,c,order='lex')
gb=[sp.expand(p.as_expr()) for p in GB.polys]
assert 2*a+3*b-5 in gb
assert b**2-2*b+1 in gb
assert c in gb
fac8sol=sp.expand(fac8.subs({a:1,b:1,c:0}))
assert fac8sol==sp.expand(t**3*(1+t)**5)

# General exponent and degree formulas.
for m in range(5,21):
    if m%2:
        d=(m-1)//2; e=(m+1)//2; D=3*m+2
        assert e-d==1
    else:
        d=m//2-1; e=m//2+1; D=3*m+4
        assert e-d==2
    assert d+e==m
    assert d+5*e==D
    assert d+5*e-1==D-1

print('m=6 square-cubic obstruction: VERIFIED (forces k=0)')
print('m=6 cube-quadratic obstruction: VERIFIED')
print('m=7 A2^2 B1^3 obstruction: VERIFIED; resultant=24869376')
print('m=8 square-quartic obstruction: VERIFIED')
print('m=8 A1^2 B2^3 obstruction: VERIFIED (forces k=0)')
print('minimal direction exponent/degree formulas m=5..20: VERIFIED')
print('Together with the logarithmic-derivative proof, this covers all m>=6.')
