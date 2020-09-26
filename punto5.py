# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:02:24 2020

@author: maher
"""
import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
import scipy as sp
import math as m
import random

t = np.linspace(-0.1, 0.1, 1000)
noise = np.random.(0, 1)
Fs=4 #frecuencia de muestreo
plt.subplot(211)
plt.title(r'Grafica de la Señal: 15*np.sin(2*np.pi*33*t) + 382*np.sin(2*np.pi*40*t)+ 611*np.sin(2*np.pi*20*t) con RMS');
s=115*np.sin((100/2*m.pi)*t) + 382*np.sin((204/2*m.pi)*t)+ 611*np.sin((306/2*m.pi)*t)+noise;
plt.plot(t,s);
plt.plot(t,1108/sqrt(2)+t);
plt.xlabel('t');
plt.ylabel('x(t)');
plt.xlim([-0.1, 0.1]);
plt.subplot(212)
#plt.title('Espectro de la señal')
plt.magnitude_spectrum((115*np.sin(100*t) + 382*np.sin(204*t)+ 611*np.sin(306*t)),Fs);
plt.xlim([0,0.1]);
plt.show()