#!/usr/bin/python
# coding: utf-8

#################################################"    
##                 MODULES                  #####"
#################################################"
import matplotlib.pyplot as plt
import numpy as np
#################################################"

# Parameters
N = 500                     # Number of sampling
Tmax = 2.0                  # Max time
Te = Tmax/N                  # Delta time between each measurements
f1=1                         # Acquisition frequency
t = np.arange(0, Tmax, Te)   # Time vector

# Functions
u1=0.5*1.0*np.cos(2*np.pi*f1*t)
u2=0.3*np.cos(2*2*np.pi*f1*t-np.pi/3)

u=u1+u2

# Figure
fig1=plt.figure(figsize=(10,5))
plt.plot(t,u, 'k', label='u')
#plt.hold(True)
plt.plot(t,u1, 'r--', label='u1')
plt.plot(t,u2, 'g--', label='u2')

plt.legend()
plt.xlabel("t")
plt.ylabel("u")
plt.axis([0,2,-2,2])
plt.grid()


#   Save the figure
fig1.savefig('Figure_TD1',dpi=200)

plt.show()

