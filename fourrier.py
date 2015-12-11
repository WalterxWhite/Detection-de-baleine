import random
import numpy as np
import aifc
from matplotlib import mlab
import pylab as pl
import csv
import sys
from scipy.fftpack import fft
import matplotlib.pyplot as plt


def ReadAIFF(file):
	""" Read AIFF and convert to numpy array
		Args:
			file: string
				file to read
		Returns:
			numpy array containing whale audio clip
	"""
	
	s = aifc.open(file ,'r')
	nFrames = s.getnframes()
	strSig = s.readframes(nFrames)
	tab = np.fromstring(strSig,np.short).byteswap()
	np.savetxt('test.txt', tab) 
	data = np.loadtxt('test.txt')
	return tab
	

"""Lecture et enregistrement, puis affichage"""
datafolder = "/home/villebon/Documents/train1.aiff"
tab = ReadAIFF(datafolder)

"""FFT et affichage du spectre"""
"""Lecture et enregistrement, puis affichage"""
datafolder = "/home/villebon/Documents/train1.aiff"
tab = ReadAIFF(datafolder)

"""FFT et affichage du spectre"""
z = np.fft.fft(tab)
print(len(z))
w = np.fft.rfft(tab)
x = np.arange(len(w))*2
print(len(w))
#plt.plot(z, color ='red')
plt.plot(x, w, color = 'green')
plt.show()

