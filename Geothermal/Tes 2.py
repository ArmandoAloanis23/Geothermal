

"""         NDA JADI            """
from pyXSteam.XSteam import XSteam
steamT = XSteam(XSteam.UNIT_SYSTEM_MKS)

import numpy as np 
import matplotlib.pyplot as plt


temperatur = np.linspace(1,374,1000,dtype= int)
print(temperatur)

h = steamT.hV_t(temperatur)
print(h)

plt.plot(temperatur,h)
plt.show()
