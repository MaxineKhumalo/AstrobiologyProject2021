# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import exoplasim as exo
import matplotlib.pyplot as plt
import numpy as np
import pickle

earthlike = exo.Model(resolution='T21', ncpus=1, workdir='earthlike_run', modelname='Earth-like', outputtype='.npz')

P = [1, 10, 100]

for i in P:
    print('P = ', P)
    earthlike.configure(startemp=5800.0, flux=1367.0,                              # Stellar parameters
                        eccentricity=0.016715,obliquity=23.441,fixedorbit=True,    # Orbital parameters
                        synchronous=False,rotationperiod=1.0,                       # Rotation
                        radius=1.0,gravity=9.80665,#aquaplanet=True,               # Bulk properties
                        pN2=i*(1-360e-6),pCO2=i*360e-6,ozone=True,                 # Atmosphere
                        timestep=30.0,snapshots=720,physicsfilter="gp|exp|sp")     # Model dynamics
    earthlike.exportcfg();
    earthlike.run(years=1,crashifbroken=True);
    print('running...','P=',i)
    lon = earthlike.inspect("lon")
    lat = earthlike.inspect("lat")
    ts = earthlike.inspect("ts",tavg=True)
    im=plt.pcolormesh(lon,lat,ts,cmap="RdBu_r",vmin=273.15-60.0,vmax=273.15+60.0,shading="Gouraud")
    plt.contour(lon,lat,ts,[273.15,],colors=['gray',])
    plt.colorbar(im,label="Surface Temperature [K]")
    plt.xlabel("Longitude [deg]")
    plt.ylabel("Latitude [deg]")
    plt.title("Earthlike with P={} bar Surface Temperature".format(str(i)))
    plt.savefig("P={}bar_Surface_Temperature2.png".format(str(i)),dpi=300)
    with open("P={}bar_Surface_Temperature2.txt".format(str(i)), "wb") as fp:   #Pickling
        pickle.dump([lon,lat,ts], fp)
    print("P =",i)

e = [0.001, 0.01, 0.016715, 0.1, 0.3, 0.7, 0.9]

for i in e:
    earthlike.configure(startemp=5800.0, flux=1367.0,                              # Stellar parameters
                        eccentricity=e,obliquity=23.441,fixedorbit=True,    # Orbital parameters
                        synchronous=False,rotationperiod=1.0,                       # Rotation
                        radius=1.0,gravity=9.80665,#aquaplanet=True,               # Bulk properties
                        pN2=1*(1-360e-6),pCO2=1*360e-6,ozone=True,                 # Atmosphere
                        timestep=30.0,snapshots=720,physicsfilter="gp|exp|sp")     # Model dynamics
    earthlike.exportcfg();
    earthlike.run(years=1,crashifbroken=True);
    print('running...','e=',i)
    lon = earthlike.inspect("lon")
    lat = earthlike.inspect("lat")
    ts = earthlike.inspect("ts",tavg=True)
    im=plt.pcolormesh(lon,lat,ts,cmap="RdBu_r",vmin=273.15-60.0,vmax=273.15+60.0,shading="Gouraud")
    plt.contour(lon,lat,ts,[273.15,],colors=['gray',])
    plt.colorbar(im,label="Surface Temperature [K]")
    plt.xlabel("Longitude [deg]")
    plt.ylabel("Latitude [deg]")
    plt.title("Earthlike with e={} Surface Temperature".format(str(i)))
    plt.savefig("e={}_Surface_Temperature2.png".format(str(i)),dpi=300)
    with open("e={}_Surface_Temperature2.txt".format(str(i)), "wb") as fp:   #Pickling
        pickle.dump([lon,lat,ts], fp)
    print("e =",i)
    
o = [0, 1, 10, 23.441, 45, 90, 100, 135, 180]

for i in o:
    earthlike.configure(startemp=5800.0, flux=1367.0,                              # Stellar parameters
                        eccentricity= 0.016715,obliquity=i,fixedorbit=True,    # Orbital parameters
                        synchronous=False,rotationperiod=1.0,                       # Rotation
                        radius=1.0,gravity=9.80665,#aquaplanet=True,               # Bulk properties
                        pN2=1*(1-360e-6),pCO2=1*360e-6,ozone=True,                 # Atmosphere
                        timestep=30.0,snapshots=720,physicsfilter="gp|exp|sp")     # Model dynamics
    earthlike.exportcfg();
    earthlike.run(years=1,crashifbroken=True);
    print('running...','o=',i)
    lon = earthlike.inspect("lon")
    lat = earthlike.inspect("lat")
    ts = earthlike.inspect("ts",tavg=True)
    im=plt.pcolormesh(lon,lat,ts,cmap="RdBu_r",vmin=273.15-60.0,vmax=273.15+60.0,shading="Gouraud")
    plt.contour(lon,lat,ts,[273.15,],colors=['gray',])
    plt.colorbar(im,label="Surface Temperature [K]")
    plt.xlabel("Longitude [deg]")
    plt.ylabel("Latitude [deg]")
    plt.title("Earthlike with obliq={} Surface Temperature".format(str(i)))
    plt.savefig("obliq={}_Surface_Temperature2.png".format(str(i)),dpi=300)
    with open("obliq={}_Surface_Temperature2.txt".format(str(i)), "wb") as fp:   #Pickling
        pickle.dump([lon,lat,ts], fp)
    print("0 =",i)
    
    


