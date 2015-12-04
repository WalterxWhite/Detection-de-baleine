import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt
from sklearn import linear_model

def ouverture ( ):
  csv = np.genfromtxt ('train.csv', delimiter=",")
  clip_name = csv[:,0]
  label = csv[:,1]

  
