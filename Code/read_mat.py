
import scipy.io as sio  
import matplotlib.pyplot as plt  
import numpy as np  
  

matfn=r'C:\Users\Windows\Desktop\2018Win\Heart Project\code\A00001.mat'  
data=sio.loadmat(matfn)  
  
print (data['A'])