#!/usr/bin/env python

import os
import pandas as pd
import numpy as np
import awkward
import uproot_methods

if __name__ == '__main__':
	df = pd.read_hdf('/Users/halil/cernbox/ML-data/v0/test.h5', key='table')
	#print(df)
	print(list(df.columns))