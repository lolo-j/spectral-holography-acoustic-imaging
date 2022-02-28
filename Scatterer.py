#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.special as ss
from Coeff.py import Coefficient

# In[18]:


class Scatterer(object):
    def __init__(self,
                 a_p=1.,   # radius of scatterer [m]
                 p_p=1.5,  # density of scatterer 
                 c_p=0.,   # speed of sound in scatterer
                 **kwargs):
        self.a_p = a_p
        self.p_p = p_p
        self.c_p = c_p
        
    @property
    def a_p(self):
        '''Radius of scatterer [m]'''
        if self._a_p.size == 1:
            return self._a_p.item()
        else:
            return self._a_p

    @a_p.setter
    def a_p(self, a_p):
        self._a_p = np.asarray(a_p, dtype=float)

    @property
    def p_p(self):
        '''density of scatterer'''
        if self._p_p.size == 1:
            return self._p_p.item()
        else:
            return self._p_p

    @p_p.setter
    def p_p(self, p_p):
        self._p_p = np.asarray(p_p, dtype=float)

    @property
    def c_p(self):
        '''speed of sound in scatterer'''
        if self._c_p.size == 1:
            return self._c_p.item()
        else:
            return self._c_p

    @c_p.setter
    def c_p(self, c_p):
        self._c_p = np.asarray(c_p, dtype=float)
        
          
    
        
    def scattered_wave(self):
        P = ss.legendre(m, monic = True)
        for i in P:
            
        f_s = 0 
        
        f = -(((-1j)**m))*((2*m+1)/(1+1j*C_m))*

# In[ ]:




