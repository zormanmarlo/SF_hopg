import matplotlib.pyplot as plt
from sys import argv
import numpy as np

## -----------------------------------------------------------------------------
## Sript to plot xvg file
## -----------------------------------------------------------------------------
plt.style.use("/Users/mdog/OneDrive - UW/misc/SF.mplstyle")
color = plt.cm.viridis(np.linspace(0, 1, 3))
# plt.rcParams['axes.prop_cycle'] = cycler.cycler('color', color)

# open files and initialize lists
filename = "11strand-rmf.dat"
file = open("data/"+filename, "r")
x_axis = []
y_axis = []

# parse file for labels and data
for line in file:
    tmp = line.split()
    x_axis.append(float(tmp[0]))
    y_axis.append(float(tmp[1]))

# highlight turn residues
turns = [[13+(i*16),14+(i*16),15+(i*16),16+(i*16)] for i in range(0,10,2)]
for i in range(len(turns)):
    arr = [i for i in turns[i]]
    plt.axvspan(arr[0], arr[-1], zorder=0, alpha=0.2, color='blue', label='turns')
turns = [[13+(i*16),14+(i*16),15+(i*16),16+(i*16)] for i in range(1,10,2)]
for i in range(len(turns)):
    arr = [i for i in turns[i]]
    plt.axvspan(arr[0], arr[-1], zorder=0, alpha=0.5, color='#ECBF51', label='turns')

plt.plot(x_axis, y_axis, color="black")
plt.tight_layout()
plt.savefig("RMSF.svg", dpi=300, transparent=True)
plt.show()
