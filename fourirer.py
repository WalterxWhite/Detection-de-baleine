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
	tab=np.fromstring(strSig,np.short).byteswap()
	np.savetxt('test.txt', tab) 
	data= np.loadtxt('test.txt', dtype='int')
	return np.fromstring(strSig,np.short).byteswap(),data	
	
def fourrier(data):
	
	# Number of sample points
	data= np.loadtxt('test.txt', dtype='int')
	N = len(data[:,0])
	# sample spacing
	T = 1.0 / 2.0
	'''x = np.linspace(0.0, N*T, N)'''
	y = data[:,0]
	yf = fft(y)
	xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
	plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
	plt.grid()
	plt.show()




datafolder = "C:/Users/Thibault/Desktop/INFORMATIQUE/BALEINE-PROJET/train6.aiff"
print ReadAIFF(datafolder)
"""txt_file = r"test.txt"
csv_file = r"test1.csv"
in_txt = open(txt_file, "r")
out_csv = csv.writer(open(csv_file, 'wb'))
file_string = in_txt.read()
file_list = file_string.split('\n')
for row in file_list:       
  	 out_csv.writerow(row)"""
print fourrier("test.txt")

