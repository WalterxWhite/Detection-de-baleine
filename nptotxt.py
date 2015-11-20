import random
import numpy as np
import aifc
from matplotlib import mlab
import pylab as pl
import csv
import sys

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
	
	np.savetxt('test.txt', np.fromstring(strSig,np.short).byteswap() ) 

	return np.fromstring(strSig,np.short).byteswap()
	

	
	

datafolder = "C:/Users/Thibault/Desktop/INFORMATIQUE/train6.aiff"
print ReadAIFF(datafolder)









"""txt_file = r"test.txt"
csv_file = r"test1.csv"

in_txt = open(txt_file, "r")
out_csv = csv.writer(open(csv_file, 'wb'))

file_string = in_txt.read()

file_list = file_string.split('\n')

for row in file_list:       
  	 out_csv.writerow(row)"""
