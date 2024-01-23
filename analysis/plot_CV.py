import matplotlib.pyplot as plt
from sys import argv
import numpy as np
import cycler
import shlex
import pickle

## -----------------------------------------------------------------------------
## Sript to plot CVs from COLVAR files 
## -----------------------------------------------------------------------------
plt.style.use("./basic.mplstyle")

colors = ["#291715", "#784542", "#EA8677"]
filenames = ["1.1", "1.4", "1.0"]
fig = plt.figure()
ax  = fig.add_subplot(111)

for i, filename in enumerate(filenames):
    # open files and initialize lists
    xvg_file = open("data/unbiased_ext/colvar_"+filename, "r")
    y_axis = []
    x_axis = []
    for line in xvg_file:
        if "@" not in line and "#" not in line:
            tmp = line.split()
            # print
            if len(tmp) != 1:
                try:
                    x_axis.append(float(tmp[0])/1000)
                    y_axis.append(float(tmp[1])-1.111) # subtracting to center at 0
                except:
                    print(line)
    plt.plot(x_axis, y_axis, color=colors[i])

plt.legend(["Trial$_1$", "Trial$_2$", "Trial$_3$"], fontsize=16)
# leg = ax.legend()
# for line in leg.get_lines():
#     line.set_linewidth(2.0)
# plt.legend(filenames)
# plt.xlim([0,500])
# plt.xlabel("Time (ns)")
# plt.ylabel("sigma")
# plt.xlim([-0.25,5])
plt.tight_layout()
plt.savefig("orientation.svg", dpi=300, transparent=True)
