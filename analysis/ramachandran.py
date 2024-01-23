from MDAnalysis.analysis.dihedrals import Ramachandran
import matplotlib.pyplot as plt
import MDAnalysis as mda
import numpy as np


## -----------------------------------------------------------------------------
## Script to compute dihedral angles with md analysis
## -----------------------------------------------------------------------------
plt.style.use("./basic.mplstyle")

# define systems
systems = ["SC_up_0", "SC_down_0"]
names = ["Alanine residues protruding", "Glycine residues protruding"]

fig, ax = plt.subplots(2,1)
for i, system in enumerate(systems):
    print(system)

    # load trajectories
    trj_path = "/Users/mdog/research/hopg/jobs/one_protein_hopg/"+system+"/full.xtc"
    top_path = "/Users/mdog/research/hopg/jobs/one_protein_hopg/"+system+"/em/em.gro"
    u = mda.Universe(top_path, trj_path)

    # run analysis
    turns = [14,15,16, 30,31,32, 46,47,48, 62,63,64, 78,79,80, 94,95,96, 110,111,112, 126,127,128, 142,143,144, 158,159,160]
    selection = "not resname GP001 and not resname SOL and ("
    for turn in turns:
        selection += "resid "+str(turn)+" "
        if turn != 160:
            selection +="or "
    selection += ")"

    r = u.select_atoms(selection)
    R = Ramachandran(r).run(start=1150, stop=1300)
    ax[i].hist2d(R.angles[:,:,0].flatten(), R.angles[:,:,1].flatten(), bins=[75,75], cmap="Purples")
    ax[i].set_title(names[i], size="small")
    # left / right turn specific analysis
    # left_turns = [14,15,16,46,47,48,78,79,80,110,111,112,142,143,144]
    # right_turns = [30,31,32,62,63,64,94,95,96,126,127,128,158,159,160]
    #
    # selection = "not resname GP001 and not resname SOL and ("
    # for turn in left_turns:
    #     selection += "resid "+str(turn)+" "
    #     if turn != 144:
    #         selection +="or "
    # selection += ")"
    #
    # r = u.select_atoms(selection)
    # R = Ramachandran(r).run()
    # # print(R.angles.shape)
    # # print(R.angles[:,:,1])
    # ax[i,0].hist2d(R.angles[:,:,0].flatten(), R.angles[:,:,1].flatten(), bins=[75,75], cmap="Oranges")
    # ax[i,0].set_title(names[i]+" left-side turns", size="small")
    #
    # selection = "not resname GP001 and not resname SOL and ("
    # for turn in right_turns:
    #     selection += "resid "+str(turn)+" "
    #     if turn != 160:
    #         selection +="or "
    # selection += ")"
    # r = u.select_atoms(selection)
    # R = Ramachandran(r).run()
    # ax[i,1].hist2d(R.angles[:,:,0].flatten(), R.angles[:,:,1].flatten(), bins=[75,75], cmap="Blues")
    # ax[i,1].set_title(names[i]+" right-side turns", size="small")

for a in ax.flat:
    a.tick_params(axis='both',labelsize=6)

# ax[1,0].set_xlabel(r"$\phi$", weight="bold", size="small")
# ax[1,0].set_ylabel(r"$\psi$", weight="bold", size="small")
# ax[1,1].set_xlabel(r"$\phi$", weight="bold", size="small")
# ax[0,0].set_ylabel(r"$\psi$", weight="bold", size="small")

# plt.show()
plt.tight_layout()
plt.savefig("rama.svg", dpi=400, transparent=True)
