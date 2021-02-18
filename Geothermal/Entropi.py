from pyXSteam.XSteam import XSteam
import matplotlib.pyplot as plt
import numpy as np

steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS)

#Temperatur
t = np.arange(0,373.9,0.01)

#Entropi Fluida fasa cair
nsL_t = np.frompyfunc(steam_table.sL_t, 1, 1) #jangan lupa ini supaya nda error sama dengan tadi
sL_t = nsL_t(t)
garis1, = plt.plot(sL_t,t)
plt.setp(garis1, linewidth =1, color = 'b')

#Entropi Fluida fasa uap
nsV_t = np.frompyfunc(steam_table.sV_t, 1, 1) #jangan lupa ini supaya nda error sama dengan tadi
sV_t = nsV_t(t)
garis2, = plt.plot(sV_t,t)
plt.setp(garis2, linewidth =1, color = 'r')

plt.ylabel("Temperatur (degC)")
plt.xlabel("Entropi Fluida (kJ/kg K)")



plt.show()

