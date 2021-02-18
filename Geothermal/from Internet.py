from pyXSteam.XSteam import XSteam
import matplotlib.pyplot as pyplot
import numpy as np

steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS)

p = np.arange(-100.0, 250.0, 1.0)
ntsat_p = np.frompyfunc(steam_table.tsat_p, 1, 1)
tsat = ntsat_p(p)
line1, = pyplot.plot(tsat, p)
pyplot.xlabel("t")
pyplot.ylabel("p")
pyplot.setp(line1, linewidth=1, color='b')
pyplot.show()