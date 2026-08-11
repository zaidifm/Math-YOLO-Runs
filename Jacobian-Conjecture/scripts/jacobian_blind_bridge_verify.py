import sympy as sp
x,y,z,a,W = sp.symbols('x y z a W')
r0,r1,r2 = sp.symbols('r0 r1 r2')

# BLIND2 chart
v = 1 + 2*x*y
L = -1 + 3*x*y + x**2*z
K = y + 6*x*y**2 + x*z + 2*x**2*y*z
Wxyz = sp.expand(x*L)
axyz = v/x
bxyz = sp.expand(1 + axyz*Wxyz)
cxyz = sp.expand(axyz*bxyz)
print('b-xK:', sp.factor(bxyz - x*K))
print('c-vK:', sp.factor(cxyz - v*K))
print('cW-b(b-1):', sp.factor(cxyz*Wxyz - bxyz*(bxyz-1)))

# Abstract boundary ring and derivation D = d/da on the A^2 chart
b,c = sp.symbols('b c')
# D(W)=0, D(b)=W, D(c)=2b-1
rel = c*W - b*(b-1)
Drel = sp.expand((2*b-1)*sp.diff(rel,c) + W*sp.diff(rel,b))
print('D preserves relation:', sp.factor(Drel))

# Unified canonical deformation: R(t), t=b-1. Check formula for quadratic generic R.
t = b-1
R = r0 + r1*t + r2*t**2
Rp = sp.diff(R,b)  # dt/db = 1
# g in hidden variables: a^2 b^3 R. replace a=c/b for abstract ring expression
# ring expression g = b*c^2*R
g_ring = sp.expand(b*c**2*R)
# D acting on any f(b,c,W): W f_b + (2b-1) f_c
Dg_ring = sp.expand(W*sp.diff(g_ring,b)+(2*b-1)*sp.diff(g_ring,c))
# expected formula using cW=b(b-1)
expected_Dg = sp.expand(b*c*((5*b-3)*R + b*(b-1)*Rp))
print('Dg raw difference factor:', sp.factor(Dg_ring-expected_Dg))
# Difference should be multiple of relation; divide polynomially by relation with groebner reduction
G=sp.groebner([rel], c,b,W,r0,r1,r2, order='lex')
print('Dg reduced difference:', G.reduce(Dg_ring-expected_Dg)[1])

# a Dg-g expected; compute in hidden a,b with W relation b=1+aW separately
a0=sp.symbols('a0')
bh=1+a0*W
th=a0*W
Rh=r0+r1*th+r2*th**2
gh=a0**2*bh**3*Rh
dgh=sp.diff(gh,a0)
# translate expected ring formulas back b=bh,c=a*b
ch=a0*bh
ExpU=bh*ch*((5*bh-3)*Rh+bh*(bh-1)*(r1+2*r2*th))
ExpS=ch**2*((4*bh-3)*Rh+bh*(bh-1)*(r1+2*r2*th))
print('hidden d/da formula:', sp.factor(dgh-ExpU))
print('hidden a*d/da-g formula:', sp.factor(a0*dgh-gh-ExpS))

# Finite-jet equivalence for cubic H with symbolic coeffs, solve conditions
h0,h1,h2,h3=sp.symbols('h0 h1 h2 h3')
tvar=sp.symbols('t')
H=h0+h1*tvar+h2*tvar**2+h3*tvar**3
conds=[sp.expand(H.subs(tvar,-1)), sp.expand(sp.diff(H,tvar).subs(tvar,-1)-1), sp.expand(sp.diff(H,tvar,2).subs(tvar,-1))]
sol=sp.solve(conds,[h0,h1,h2],dict=True)
print('jet solve cubic:', sol)
if sol:
    Hsol=sp.expand(H.subs(sol[0]))
    print('H-(1+t) factor:', sp.factor(Hsol-(1+tvar)))

# Leading monomial vectors for W,b,c from xyz
# total degree and leading terms by total degree, lex for display
polys={'W':Wxyz,'b':bxyz,'c':cxyz}
for name,p in polys.items():
    P=sp.Poly(p,x,y,z)
    maxdeg=max(sum(m) for m,_ in P.terms())
    tops=[(m,coef) for m,coef in P.terms() if sum(m)==maxdeg]
    print(name,'degree',maxdeg,'top terms',tops)
