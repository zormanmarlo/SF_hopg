import matplotlib.pyplot as plt
import MDAnalysis as mda
import numpy as np
import pickle

## -----------------------------------------------------------------------------
## Script to compute contacts with mdanalysis
## Can be used for protein-water, protein-protein, protein-graphite, etc
## -----------------------------------------------------------------------------

plt.style.use("./basic.mplstyle")
colors = ["salmon", "darkslategray"]

## -----------------------------------------------------------------------------
# file paths
systems = ["SC_up_0", "SC_down_0"]
residue_contacts = []

for i, system in enumerate(systems):
    trj_path = "/Users/mdog/research/hopg/jobs/one_protein_hopg/"+system+"/full.xtc"
    top_path = "/Users/mdog/research/hopg/jobs/one_protein_hopg/"+system+"/em/em.gro"
    turn_string = "resnum 160:176 or resnum 1:12 or resnum 13 or resnum 14 or resnum 15 or resnum 16 or resnum 45 or resnum 46 or resnum 47 or resnum 48 or resnum 77 or resnum 78 or resnum 79 or resnum 80 or resnum 109 or resnum 110 or resnum 111 or resnum 112 or resnum 141 or resnum 142 or resnum 143 or resnum 144 or resnum 173 or resnum 174 or resnum 175 or resnum 176"

    u = mda.Universe(top_path, trj_path)
    residue_contacts = []
    print(len(u.trajectory))
    for ts in u.trajectory[::10]:
        if ts.time%100 == 0:
            print(ts.time)
        # change atom selection to get other contacts 
        residue_contacts.append(len(u.select_atoms("resname SOL and around 5 (resname GP001 and index 40000:70000)")))

    pickle.dump(residue_contacts, open("data/"+system+"_surface_waters.p", "wb"))
    # residue_contacts = pickle.load(open("data/"+system+"_surface_and_protein_waters.p", "rb"))[275:-1]
    plt.plot([i/len(residue_contacts)*110 for i in range(len(residue_contacts))], residue_contacts, color=colors[i])
    # plt.plot(residue_contacts, color=colors[i])


## -----------------------------------------------------------------------------
# plot
# turns = [[13+(i*16),14+(i*16),15+(i*16),16+(i*16)] for i in range(0,10)]
# for i in range(len(turns)):
#     arr = [i for i in turns[i]]
#     plt.axvspan(arr[0], arr[-1], zorder=0, alpha=0.2, color='orange', label='turns')

# plt.xlabel("Residue", weight="bold")
# plt.ylabel("Water contacts", weight="bold")
# plt.ylim([0,30])
# plt.savefig("figs/1x4_fiber_down_per_residue_fiber_water_contacts.png")

leg = plt.legend(["Alanine residues protruding", "Glycine residues protruding"], loc="best", prop={"size":12})
plt.axvline(x = 10, color = 'gray', linestyle="--")
plt.axvspan(-2.5, 10, alpha=0.2)
plt.xlim(-2.5,115)
plt.rcParams["figure.figsize"] = (8,8)
# for line in leg.get_lines():
#     line.set_linewidth(2.0)
# plt.xlabel("Time (ns)")
# plt.ylabel("Water-Protein Contacts")
plt.tight_layout()
plt.savefig("contacts.svg", dpi=300, transparent=True)
plt.show()
