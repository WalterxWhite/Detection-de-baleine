import numpy as np
import csv

def Trie (csv):
  csv = np.genfromtxt ('train.csv', delimiter=",")
  clip_name = csv[1:,0]
  label = csv[1:,1]
  taille=len(clip_name)
  
  for i in range (taille):
    if label[i]==1:
      baleine_franche[k]=clip_name[i]
      k+=1
    else : 
      i+=1

  baleine_franche = csv.writer(open("Baleine_franche.csv", "wb"))
import numpy as np
import csv

def trie (file):
  file = 'train.csv'
  data = np.opentxt(file)
  clip_name = data[:,0]
  label = data[:,1]
  taille=len(clip_name)
  k=0
  for i in range (taille):
    baleine_franche[]
    if label[i]==1:
      baleine_franche[k]=clip_name[i]
      k+=1
    else : 
      i+=1
  baleine_franche = csv.writer(open("Baleine_franche.csv", "wb"))

  return baleine_franche


def main ():

  trie(file)

if __name__=='__main__' : 
   main()
