#!/usr/bin/env python
import sys
import os
#import pandas as pd
import h5py as h5
import tables
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import colors, cm


if __name__ == "__main__":
	###### Configuration ########
    do_events = 100 # -1 for all
    val_ratio = 0.3
    #############################

    if len(sys.argv) == 1:
	    fname = 'train'
	    fno = '10'
    else:
        fname = sys.argv[1]
        fno = sys.argv[2]

    input_file="data/%s_ntuple_merged_%s.h5"%(fname,fno)
    df = h5.File(input_file, "r" )
    print ('opened data file: {}'.format(input_file))
    for key in df:
        print(df[key])

    sys.exit()
    key='fj_gen_pt'
    key='pfcand_ptrel'
    #print(list(df[key]))
    events = (len(df[key]))
    for i in range(1, 10):
        print(i, df[key])
    #print(events)
#    sys.exit()

    #for item  in df.attrs.keys():
    #    print(item + ": " , df.attrs[item])

    vector_keys = [ "pfcand_ptrel", "pfcand_phirel", "pfcand_etarel"]
    keys = []
    for key in vector_keys:
        keys.append(df["{}".format(key)])

    events = (len(df["pfcand_ptrel"]))
    print ('file has {} events'.format(events))
    n = events if do_events == -1 else do_events
    print ('will analyze {} events'.format(n))
        
    c= int(n * val_ratio)
    labels = [0]*(n-c) + [1]*c

    pt = keys[0]
    phi = keys[1]
    eta = keys[2]
    all_images = []
    for si in range(1, n):
        #si = 10000+i
        if si % 1000 == 0: print (si)
        pt_seri = pd.Series(pt[si])
        eta_seri = pd.Series(eta[si])
        phi_seri = pd.Series(phi[si])
        #print (phi_seri[0:30])
        #sys.exit()
        images = []
        new_matrices = []
        #for a in range(1):
        #print("Centering")
        eta_seri = eta_seri.subtract(eta_seri[0], axis=0)
        phi_seri = phi_seri.subtract(phi_seri[0], axis=0).add(np.pi).mod( 2 * np.pi).subtract(np.pi)
