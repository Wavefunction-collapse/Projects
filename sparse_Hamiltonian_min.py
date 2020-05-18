# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 01:58:27 2020

@author: Paul, Nikolai 
"""

import scipy.sparse as sp
import numpy as np
import time
import cProfile
import seaborn as sb
import matplotlib.pyplot as plt


def Basis( n ):
    Szbasis = np.arange( 0, 2**n, 1)
    print(" ")
    print( "length of chain is:", n, "  ;     size of Basis:", 2**n )
    return( Szbasis )

def Lanczos( A, n, m ):
    #calculates m eigenvalues of A
    print( " " )
    print( "solving using Lanczos algorithm ")
    from scipy.sparse.linalg import eigsh        
    start = time.time()
    N = 2 ** n
    r0 = np.random.rand( N , 1 )
    r0 = r0 / np.linalg.norm(r0)
    v0 = 0
    row = []    ;    col = []    ;    val = []      #to construct scipy.sparse coo matrix
    for k in range(m):
        b  = np.linalg.norm( r0 ) #sp.linalg.norm( r0 )
        v1 = r0 / b
        a  = ( v1.T ).dot( A.dot( v1 ) )
        r1 = (A -  sp. diags( a* np.ones( N ), [0] ) ).dot(v1) - b * v0 
        row.append( k )
        col.append( k )
        val.append( a )
        #T[ k, k ] = a, see function Hamiltonian
        if not (k==0):
            row.append( k -1 )
            col.append( k )
            val.append( b )
            
            row.append( k )
            col.append( k -1 )
            val.append( b )
            
            #T[ k-1, k ] = b    and    T[ k, k-1 ] = b 
        v0 = v1
        r0 = r1
    T = sp.coo_matrix((val, (row, col)), shape=( m , m ), dtype= float )
    (evalues, evectors ) = eigsh( T, m-1)
    end = time.time()
    print("done! Computation time of eigenvalues :" , end - start )
    return( evalues, evectors )

    
def Hamiltonian( Basis, J, n ):
    print()
    print( "creating Hamiltonian now" )
    start = time.time()
    row = []    ;    col = []    ;    val = []      #to construct scipy.sparse coo matrix
    for state in Basis:
        bin_state = np.binary_repr(state, width = n)
        for i in range( n ):
            j = (i+1)%n
            #   check for matching bits
            if bin_state[i] == bin_state[j]:
                row.append( state )
                col.append( state )
                val.append( J/4 )
                #   is equvalent to,  H[ state, state ] += J/4
                #   as values with same indexes are summed over. 
            else:
                row.append( state )
                col.append( state )
                val.append( - J/4 )
                
                mask = 2**(n-i-1)+2**(n-j-1)        # in binary this represents ones at sites i and j
                flipped = state ^ mask
                #    ^ acts as bitwise XOR operator, so mask flips bits at site i 
                
                row.append( state )
                col.append( flipped )
                val.append( J/2 )
    H = sp.coo_matrix((val, (row, col)), shape=( 2**n , 2**n )) #assambling the sparse matrix    
    end = time.time()
    print( "done! Computation time of Hamiltonian:", end - start, "s")
    H = H.tocsr()
    #   csr is much better format for calculation than coo
    return( H )
            
    
n = input('Please choose the size of your basis:\n')
n=int(n)
b = Basis( n )
H = Hamiltonian( b, 1.0, n) 
m = input('Please choose the number of iterations you want to have computed:\n')
m=int(m)


evl, evs = Lanczos( H, n , m )
print(  evl[:] ) 

#plt.plot(evl,np.ones(m-1), '+')  #here the points of convergence of the eigenvalues can be observed 
#plt.xlabel("Numerical values of the eigenvalues")
#plt.ylabel("Iterations")
# plt.ylim(0,1)
#plt.show()
#heat_map = sb.heatmap(evs, cbar_kws={'label': 'Range of the values'}) #heatmap of the eigenvectors
#plt.xlabel("Values of the eigenvectors")
#plt.ylabel("Values of the eigenvectors")
#plt.show( ) 
#plt.scatter(evl[:10], b[:10]) #eigenvalues plotted against the size of the basis

#plt.show()
  # 0 to 15 point radii

#cProfile.run('Lanczos(H,n, m)') #to measure performance exactly
#cProfile.run('Hamiltonian(b, 1.0, n)')


#minimize(evl, n, method='Nelder-Mead')
#minimize(evl, )

 
#   These should be our ground energies
#   N=2: E2 = -1.5
#   N=5: E5 = -1.868
#   N=12: E6 = -5.38738v


