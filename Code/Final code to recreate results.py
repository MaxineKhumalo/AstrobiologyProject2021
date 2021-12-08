# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import exoplasim as exo
import pickle

earthlike = exo.Model(resolution='T21', ncpus=1, workdir='earthlike_run', modelname='Earth-like', outputtype='.npz')

#Synchronous    
o = [0, 1, 10, 23.441, 45]

for i in o:
    earthlike.configure(startemp=5800.0, flux=1367.0,                              # Stellar parameters
                        eccentricity= 0.016715,obliquity=i,fixedorbit=True,    # Orbital parameters
                        synchronous=True,rotationperiod=1.0,                       # Rotation
                        radius=1.0,gravity=9.80665,#aquaplanet=True,               # Bulk properties
                        pN2=1*(1-360e-6),pCO2=1*360e-6,ozone=True,                 # Atmosphere
                        timestep=30.0,snapshots=720,physicsfilter="gp|exp|sp")     # Model dynamics
    earthlike.exportcfg();
    earthlike.run(years=1,crashifbroken=True);
    print('running...','o=',i)
    lon = earthlike.inspect("lon")
    lat = earthlike.inspect("lat")
    ts = earthlike.inspect("ts",tavg=True)
    with open("obliq={}.txt".format(str(i)), "wb") as fp:   #Pickling
        pickle.dump([lon,lat,ts], fp)
    print("o =",i)

    
#Asynchronous  
o = [0, 1, 10, 23.441, 45, 90]

for i in o:
    earthlike.configure(startemp=5800.0, flux=1367.0,                              # Stellar parameters
                        eccentricity= 0.016715,obliquity=i,fixedorbit=True,    # Orbital parameters
                        synchronous=True,rotationperiod=1.0,                       # Rotation
                        radius=1.0,gravity=9.80665,#aquaplanet=True,               # Bulk properties
                        pN2=1*(1-360e-6),pCO2=1*360e-6,ozone=True,                 # Atmosphere
                        timestep=30.0,snapshots=720,physicsfilter="gp|exp|sp")     # Model dynamics
    earthlike.exportcfg();
    earthlike.run(years=1,crashifbroken=True);
    print('running...','o=',i)
    lon = earthlike.inspect("lon")
    lat = earthlike.inspect("lat")
    ts = earthlike.inspect("ts",tavg=True)
    with open("obliq={}_async.txt".format(str(i)), "wb") as fp:   #Pickling
        pickle.dump([lon,lat,ts], fp)
    print("o =",i)
