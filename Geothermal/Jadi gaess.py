from pyXSteam.XSteam import XSteam
steamT = XSteam(XSteam.UNIT_SYSTEM_MKS)

import numpy as np 
import matplotlib.pyplot as plt

"""
for t in range(1,100):
    h = steamT.hV_t(t)
    print("Nilai entalpi uap untuk",t,"adalah",h)
"""
t = np.arange(1,374,1.0)
#print(t)

# entalpi fasa cair
iterasi = (steamT.hL_t(t) for t in range (1,374)) #harus pakai iterasi
h1 = np.fromiter(iterasi, dtype = float)
#print(h1)
plt.plot(t,h1)


# entalpi fasa uap
iterasi = (steamT.hV_t(t) for t in range (1,374)) #harus pakai iterasi
h2 = np.fromiter(iterasi, dtype = float)
#print(h2)
plt.plot(t,h2)


plt.show()
