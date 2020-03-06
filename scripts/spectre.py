#!/usr/bin/env python3

import re
import numpy as np
import matplotlib.pyplot as plt

#reg_e_plus = re.compile(r'.*Particle = e\+\,.*')
reg_e_minus = re.compile(r'.*Particle = e\-\,.*')
#reg_gamma = re.compile(r'.*Particle = gamma\,.*')
l_values_e_plus = []
l_values_e_minus = []
l_values_gamma = []
with open('../test4.txt') as fichier:    
    lines = fichier.readlines()
    for line_num, line in enumerate(lines):
        if re.search(reg_e_plus, line):
            l_values_e_plus.append(float(re.split('\s*',lines[line_num+4])[5]))
        elif re.search(reg_e_minus, line):
            l_values_e_minus.append(float(re.split('\s*',lines[line_num+4])[5]))
        elif re.search(reg_gamma, line):
            l_values_gamma.append(float(re.split('\s*',lines[line_num+4])[5]))

#plt.hist(l_values_e_plus, bins=1000, histtype='step', color = 'yellow', edgecolor = 'red')
plt.hist(l_values_e_minus, bins=1000, histtype='step', color = 'yellow', edgecolor = 'yellow')
plt.xlabel('Energy(MeV)')
plt.ylabel('nombre of particles')
plt.title('Beta_spectrum')
plt.savefig('../eminus.png') 


print(np.histogram(np.array(l_values_e_plus),bins=1000))
print(np.histogram(np.array(l_values_e_minus),bins=1000))
print(np.histogram(np.array(l_values_gamma),bins=1000))
