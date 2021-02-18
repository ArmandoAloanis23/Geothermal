# sumur 1
from pyXSteam.XSteam import XSteam
import matplotlib.pyplot as plt
import numpy as np

steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS)

D = np.array (([810, 710, 610, 510, 410, 310, 210, 110, 10, -90, -190, -290, -390, -440, -490, -540, -590, -640, -690, -740, -790,-840, -890, -915]))

T = np.array (([32.1, 66.6, 89.3, 123.4, 150.0, 168.4, 192.5, 201.2, 220.6, 232.7, 243.7, 264.3, 304.6, 311.7, 314.7, 317.4, 320.0, 322.3, 322.9, 322.7, 323.0, 325.4, 327.3, 329.7]))

P = np.array (([70.4, 72.0, 73.3, 74.3, 75.0, 75.7, 76.6, 77.8, 81.1, 88.3, 94.7, 100.9, 107.5, 110.5, 113.4, 116.4, 119.2, 122.1, 124.8, 127.4, 129.9, 132.7, 135.0, 135.6]))

nbpd = np.frompyfunc(steam_table.tsat_p, 1, 1)
bpd = nbpd(P)

plt.plot(T,D)
plt.plot(P,D)
plt.plot(bpd,D)

plt.show()

