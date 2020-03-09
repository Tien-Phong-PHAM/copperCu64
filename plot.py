#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Load data from txt file (d = depth, p = profile)
f_d_edep = 'output/dose-depth-Edep.txt'
f_d_uncert = 'output/dose-depth-Edep-Uncertainty.txt'
#f_p_edep = 'output/gamma-profile-Edep.txt'
#f_p_uncert = 'output/gamma-profile-Edep-Uncertainty.txt'

d_edep = np.loadtxt(f_d_edep)
d_uncert = np.loadtxt(f_d_uncert)
size_elem=d_edep.size
deb=int(size_elem)/2
Max_elem=np.max(d_edep)
print(Max_elem)
normalisation=list()
for t in range (0,int(size_elem)) :
    normalisation.append((d_edep[t])/Max_elem*100)

#print(normalisation)



# -----------------------------------------------------------------------------
# Declare a figure with 2 rows
#fig,ax = plt.subplots(ncols=1, nrows=1, figsize=(10,10))

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(20, 10))

# X values from 0 to 100 every 1
x = np.linspace(0, 5, 50)

# First curve, gamma depth in green
#y = d_edep[int(deb):(int(size_elem))]
y=normalisation[int(deb):(int(size_elem))]
a = ax
#a = ax[0]
c1 = a.plot(x, y, 'g-', label='edep', linewidth=1)

# Second curve, gamma uncertainty in blue, share the same x axis, but use a
# different y axis
#y = d_uncert
#ax2 = a.twinx()
#c2 = ax2.plot(x, y, 'b-', label='$\sigma$ (uncertainty)')

# Add the legend and the title
#lns = c1+c2
lns = c1
labs = [l.get_label() for l in lns]
a.legend(lns, labs, loc=0)
a.set_title('Depth deposited energy')
a.set_xlabel('Distance in mm')
a.set_ylabel('Deposited energy in MeV')
#ax2.set_ylabel('Uncertainty')

#plt.show()

plt.savefig('Profile de dose en profondeur.png')
