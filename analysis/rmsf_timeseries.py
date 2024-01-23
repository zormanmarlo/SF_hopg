from MDAnalysis.analysis import rms, align
import matplotlib.pyplot as plt
import MDAnalysis as mda
import numpy as np
import pickle

## -----------------------------------------------------------------------------
## Script to compute rmsf with MDAnalysis
## -----------------------------------------------------------------------------
plt.style.use("./basic.mplstyle")
colors = ["#de673c", "#54a8c7"]

# Define systems
systems = ["armchair_1x4_up", "armchair_1x4_down"]

for j, system in enumerate(systems):
    # load trajectory
    trj_path = "/Users/mdog/research/hopg/jobs/fiber_hopg/"+system+"/prod/analysis.xtc"
    top_path = "/Users/mdog/research/hopg/jobs/fiber_hopg/"+system+"/prod/npt_equil.gro"
    u = mda.Universe(top_path, trj_path)
    
    # perform analysis
    avg = align.AverageStructure(u, u, select="not resname GP001 and not resname SOL and name CA", ref_frame=0).run()
    ref = avg.universe
    aligner = align.AlignTraj(u, ref, select="not resname GP001 and not resname SOL and name CA", in_memory=True).run()
    c_alphas = u.select_atoms('not resname GP001 and not resname SOL and name CA')
    R = rms.RMSF(c_alphas).run()

    pickle.dump([c_alphas, R], open("data/"+system+"_rmsf.p", "wb"))
    # c_alphas, R = pickle.load(open("data/"+system+"_rmsf.p", "rb"))

    total_resids = int(len(c_alphas)/4)
    resids_to_plot = [i.resid for i in c_alphas[0:total_resids]]
    rmsf_to_plot = []
    for i in range(total_resids):
        rmsf_to_plot.append((R.rmsf[i]+R.rmsf[i+176]+R.rmsf[i+176*2]+R.rmsf[i+176*3])/4)

    plt.plot(resids_to_plot, rmsf_to_plot)

# plot properties
plt.xlabel("Residue Number")
turns = [[13+(i*16),14+(i*16),15+(i*16),16+(i*16)] for i in range(0,10)]
for i in range(len(turns)):
    arr = [i for i in turns[i]]
    plt.axvspan(arr[0], arr[-1], zorder=0, alpha=0.2, color='orange', label='turns')

leg = plt.legend(["Alanine residues protruding", "Glycine residues protruding"], loc="best", prop={"size":10})
for line in leg.get_lines():
    line.set_linewidth(4.0)
plt.ylabel('RMSF ($\AA$)')
plt.tight_layout()
plt.savefig("single_rmsf.svg", dpi=300)
