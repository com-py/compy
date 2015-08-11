# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program: Pyplot default parameters (rcpara.py, Ch. 1, Sec. 1.C)
# J Wang, Computational modeling and visualization with Python
#
import matplotlib.pyplot as plt   
plt.rc('lines',linewidth=2) # change line style, fonts in plots
plt.rc('font',size=16)      # one group at a time
plt.rc('axes',linewidth=2)
plt.rc('figure.subplot',right=0.96)
plt.rc('figure.subplot',top=0.96)
plt.rc('figure.subplot',left=0.1)