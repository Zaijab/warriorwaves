#!/usr/bin/env python
import pandas as pd

'''Class that handles the input of datafiles to standardize io'''
class WaveIO:
    '''Constructor takes in a filename'''
    def __init__(self,filename):
        self.filename = filename
        self.dt = pd.read_csv(filename + '.dt',sep='\t',usecols=[1,2,3,4],skiprows=[0],names=['ch0','ch1','ch2','ch3']).values

    '''Creates an array for all of the time series'''
    def timeseries(self):
        #TODO Copy function
       print('i')

    '''Creates an array from file put into constructor'''
    def createarray(self):
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

                if (n == 10):
                    return a
