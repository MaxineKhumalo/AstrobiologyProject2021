# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:31:26 2021

@author: mkhumalo2021
"""

import exoplasim as exo
import matplotlib.pyplot as plt
import pickle


toi700d = exo.Model(workdir="toi700d_run",modelname="TOI-700d",
                    ncpus=1,resolution="T21",outputtype=".npz")

toi700d.configure(startemp=3480.0, flux=1167.0,                           # Stellar parameters
                  eccentricity=0.,obliquity=0.,fixedorbit=True,           # Orbital parameters
                  synchronous=True,rotationperiod=37.426,                 # Rotation
                  radius=1.19,gravity=11.9,aquaplanet=True,               # Bulk properties
                  pN2=1.47*(1-360e-6),pCO2=1.47*360e-6,ozone=False,       # Atmosphere
                  timestep=30.0,snapshots=720,physicsfilter="gp|exp|sp")  # Model dynamics
toi700d.exportcfg()

toi700d.run(years=1,crashifbroken=True)
lon = toi700d.inspect("lon")
lat = toi700d.inspect("lat")
ts = toi700d.inspect("ts",tavg=True)
im=plt.pcolormesh(lon,lat,ts,cmap="RdBu_r",vmin=273.15-60.0,vmax=273.15+60.0,shading="Gouraud")
plt.contour(lon,lat,ts,[273.15,],colors=['gray',])
plt.colorbar(im,label="Surface Temperature [K]")
plt.xlabel("Longitude [deg]")
plt.ylabel("Latitude [deg]")
plt.title("TOI 700 d Surface Temperature")

i = 'test'
plt.savefig("P={}bar_Surface_Temperature.png".format(str(i)),dpi=300)
with open("P={}bar_Surface_Temperature.txt".format(str(i)), "wb") as fp:   #Pickling
    pickle.dump([lon,lat,ts], fp)
print("P =",i)