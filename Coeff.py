#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.special as ss
from Scatterer import Scatterer


def Coefficient(Scatterer):

    def find_coeff(self,w,m):
            k = w/343
            k_p = (343/self.c_p)*k
            alpha = m*ss.spherical_jn(m-1,k*self.a_p)-(m+1)*ss.spherical_jn(m+1,k*self.a_p)
            alpha_p = m*ss.spherical_jn(m-1,k_p*self.a_p)-(m+1)*ss.spherical_jn(m+1,k_p*self.a_p)
            beta = m*ss.spherical_yn(m-1,k*self.a_p)-(m+1)*ss.spherical_yn(m+1,k*self.a_p)
            g = self.p_p/1.225
            h = self.c_p/343
            C_m = (((alpha/alpha_p))*(ss.spherical_yn(m,k*self.a_p)/ss.spherical_jn(m,k_p*self.a_p)) - ((beta/alpha)*g*h))/((alpha_p/alpha)*(ss.spherical_jn(m,k*self.a_p)/ss.spherical_jn(m,k_p*self.a_p)) - g*h)
            return(C_m)