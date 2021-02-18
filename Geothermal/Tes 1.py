
"""         NDA JADI            """
from pyXSteam.XSteam import XSteam
steamT = XSteam(XSteam.UNIT_SYSTEM_MKS)

import numpy as np 
import matplotlib.pyplot as plt


temperatur = np.arange(10,100,1,dtype= int)
print(temperatur)

h = steamT.hV_t(temperatur)
print(h)

plt.plot(temperatur,h)
plt.show()
