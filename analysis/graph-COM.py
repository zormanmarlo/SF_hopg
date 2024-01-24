import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import sys
import glob

pwd = '{}/'.format(sys.path[0])
plt.style.use('/Users/christian/hopg/FIGS/SF.mplstyle')

dfs = [] #anti-stable-para 
data_files = [name.replace(pwd, '') for name in sorted(glob.glob(pwd + '*.dat'), )]


for file in data_files:
    name = str(file)
    df = pd.read_csv(file, header=0, delimiter=' ', index_col=False)
    df.columns = ["null", "frame", "d.x"]
    df.columns.name = name
    dfs.append(df)


markers = ['.', 'x', 'D']
labels = ['trial 1', 'trial 2', 'trial 3']
i = 0

plt.figure(figsize=(8, 6))
for df in dfs:
    steps = np.linspace(0, 100000, 100000)
    if len(df['d.x']) >= 100000:
        plt.plot(steps, df['d.x'][0:100000], marker = markers[i], 
        color='red', markersize=0.1, label=labels[i], alpha=0.2)
        plt.legend()
        
        plt.title('Validating Periodicity of Silk Fibroin Fibers with Unbiased Simulations')
        plt.ylabel('Center of Mass Separation (nm)', fontsize=15)
        plt.xlabel('Time (ps)', fontsize=15)
        i += 1

plt.show()
