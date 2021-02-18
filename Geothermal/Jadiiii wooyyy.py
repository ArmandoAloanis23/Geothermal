from pyXSteam.XSteam import XSteam
import matplotlib.pyplot as pyplot
import numpy as np

steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS)

#Temperatur
t = np.arange(0,373.9,0.01)

#Entalpi Fluida fasa cair
nhL_t = np.frompyfunc(steam_table.hL_t, 1, 1) #jangan lupa ini supaya nda error sama dengan tadi
hL_t = nhL_t(t)
garis1, = pyplot.plot(t,hL_t)
pyplot.setp(garis1, linewidth =1, color = 'b')

#Entalpi Fluida fasa uap
nhV_t = np.frompyfunc(steam_table.hV_t, 1, 1) #jangan lupa ini supaya nda error sama dengan tadi
hV_t = nhV_t(t)
garis2, = pyplot.plot(t,hV_t)
pyplot.setp(garis2, linewidth =1, color = 'r')

pyplot.xlabel("Temperatur (degC)")
pyplot.ylabel("Entalpi Fluida (kJ/kg)")



pyplot.show()

