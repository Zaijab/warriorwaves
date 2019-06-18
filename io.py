#!/usr/bin/env python
import pandas as pd

class IO:
    def __init__(self,filename):
        dt = pd.read_csv(filename + '.dt',sep='\t',usecols=[1,2,3,4],skiprows=[0],names=['ch0','ch1','ch2','ch3']).values
        n = 0
        a = []

        with open(filename+'.dat') as f:

            for line in f:
                if n == 0:
                    n += 1
                    header = line
                    continue
                floats = [float(x) for x in line.split()]

                a.append(floats)

                n += 1

                if (n == 8100):
                    return a
