import matplotlib.pyplot as plt
from os.path import exists
import mdtraj as md
import numpy as np
import pickle

## -----------------------------------------------------------------------------
## Script to compute dssp with MDTraj for calculation of B-strand content
## -----------------------------------------------------------------------------

plt.style.use("./basic.mplstyle")
colors = ["#de673c", "#54a8c7"]

## -----------------------------------------------------------------------------
# Systems
systems = ["SC_up_0", "SC_down_0"]
dssps = []

for system in systems:
    # calculate dssp
    trj_path = "/Users/mdog/research/hopg/one_protein_hopg/"+system+"/prod/nowat.xtc"
    top_path = "/Users/mdog/research/hopg/one_protein_hopg/"+system+"/prod/protein_hopg.gro"

    if exists("data/"+system+"_dssp.p"):
        dssp = pickle.load(open("data/"+system+"_dssp.p", "rb"))
    else:
        print("loading system")
        print(system)
        trj = md.load(trj_path, top=top_path, stride=1)
        print(len(trj))
        print("calculating dssp")
        dssp = md.compute_dssp(trj)
        pickle.dump(dssp, open("data/"+system+"_dssp.p", "wb"))

    summed = []
    if system == "unfolded":
        for frame in dssp:
            count = 0
            for res in frame[0:176]:
                if res == "E" or res == "B":
                    count += 1
            summed.append(count)
    else:
        total_residues = 176*2
        for frame in dssp:
            count = 0
            for res in frame[0:176]:
                if res == "E" or res == "B":
                    count += 1
            summed.append(count)
    dssps.append(summed)

## -----------------------------------------------------------------------------
# plot
total_time = 100
time = [total_time*i/len(dssps[0]) for i in range(len(dssps[0]))]
plt.plot(time, dssps[0][10:5295], color=colors[0])
plt.plot(time, dssps[1][10:5295], color=colors[1])

leg = plt.legend(["Alanine residues protruding", "Glycine residues protruding"], loc="best", prop={"size":12})
plt.xlabel("Time (ns)", fontsize=14)
plt.ylabel(r"Residues with $\beta$-sheet character", fontsize=14)
plt.rcParams["figure.figsize"] = (8,8)

plt.tight_layout()
plt.savefig("dssp.svg", dpi=300, transparent=True)
plt.show()
