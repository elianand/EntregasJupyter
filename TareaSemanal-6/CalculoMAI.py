import sympy as sp

from pytc2.cuadripolos import calc_MAI_impedance_ij, calc_MAI_vtransf_ij_mn, calc_MAI_ztransf_ij_mn
from pytc2.general import print_latex


'''    
+ Esquema del circuito

            
    0-----L1----2---L3--+-----3
                |       |
                C2      R
                |       |
    1-----------+-------+-----1
    
'''    

S = sp.symbols('S', complex=True)
L1, L3, C2, R = sp.symbols('L1 L3 C2 R', real=True, positive=True)

v_L1 = 1.5
v_L3 = 0.5
v_C2 = 3/4
v_R = 1
# Armo la MAI

#               Nodos:       0           1                2                  3

Ymai = sp.Matrix([  
                    [   1/(S*L1),       0,          -1/(S*L1),               0          ],
                    [       0,       S*C2+1/R,         -S*C2,              -1/R         ],
                    [   -1/(S*L1),    -S*C2,     1/(S*(L1+L3))+S*C2,     -1/(S*L3)      ],
                    [       0,        -1/R,         -1/(S*L3),          1/(S*L3)+1/R    ]
                 ])

con_detalles = False
#con_detalles = True


# Calculo la Z en el puerto de entrada a partir de la MAI
Zmai = sp.simplify(calc_MAI_impedance_ij(Ymai, 0, 1, verbose=con_detalles))
ZmaiVal = sp.simplify(Zmai.subs(L1, v_L1))
ZmaiVal = sp.simplify(ZmaiVal.subs(L3, v_L3))
ZmaiVal = sp.simplify(ZmaiVal.subs(C2, v_C2))
ZmaiVal = sp.simplify(ZmaiVal.subs(R, v_R))
print('Impedancia de entrada:')
print_latex( r'Z_{{ {:d}{:d} }} = '.format(0,1) +  sp.latex(Zmai) )
print_latex( r'Z_{{ {:d}{:d} }} = '.format(0,1) +  sp.latex(ZmaiVal) )



# Calculo la transferencia de tension a partir de la MAI
Vmai = calc_MAI_vtransf_ij_mn(Ymai, 3, 1, 0, 1, verbose=con_detalles)
VmaiVal = sp.simplify(Vmai.subs(L1, v_L1))
VmaiVal = sp.simplify(VmaiVal.subs(L3, v_L3))
VmaiVal = sp.simplify(VmaiVal.subs(C2, v_C2))
VmaiVal = sp.simplify(VmaiVal.subs(R, v_R))
print('Transferencia de tensión:')
print_latex( r'Z_{{ {:d}{:d} }} = '.format(0,1) +  sp.latex(Vmai) )
print_latex( r'Z_{{ {:d}{:d} }} = '.format(0,1) +  sp.latex(VmaiVal) )


