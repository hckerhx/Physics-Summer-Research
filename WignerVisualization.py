#----------------------------------------------------------------------
#Hang Xiang     
#Quantum Optics Summer Research
#Wigner Function Visualization (First Excited Fock State)
#June 14, 2017
#----------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

from qutip import *

#test run 

N = 20

def plot_wigner_cus(psi):
    
    #initialize figure 
    fig = plt.figure(figsize=(17, 8))
    
    
    #top view setup
    ax = fig.add_subplot(1,2,1)
    plot_wigner(psi, fig=fig, ax=ax, alpha_max=6);
    
    #3D view setup
    ax = fig.add_subplot(1,2,2, projection='3d')
    plot_wigner(psi, fig=fig, ax=ax, projection='3d', alpha_max=6);
    
    return fig
    
    
psi = basis(N,1)
#psi = (squeeze(N, 0.75j) * basis(N, 0)).unit()# - squeeze(N, -0.75j) * basis(N, 0)).unit()
plot_wigner_cus(psi)
plt.show()
