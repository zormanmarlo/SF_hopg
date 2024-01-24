from MDAnalysis.analysis import distances 
import matplotlib.pyplot as plt
import MDAnalysis as mda
import numpy as np
import argparse
import sys
from re import search
import pickle as pickle

pwd = '{}/'.format(sys.path[0])


###parsing arguments
parser = argparse.ArgumentParser(description="""understanding distances between oxygen atom
of a water molecule and the alanine-alanine turn residues of silk fibroin""")

parser.add_argument('-gro', help='gro file for MDAnalysis.', type=str, default='prod.gro')
parser.add_argument('-xtc', help='xtc file for MDAnalysis.', type=str, default='prod.xtc')
parser.add_argument('-index', help='atom index to use.', type=str, default='1-3130')

args = parser.parse_args()
index = args.index

hot = [30,31, 62,63, 94,95, 126,127, 158,159] # universal
cold = [14,15, 46,47, 78,79, 110,111, 142,143] #universal 
###generating atom groups

def calculate_water_distance(residues, cutoff):
    gro_file = args.gro
    xtc_file = args.xtc
    u = mda.Universe(gro_file, xtc_file)
    turn_selection = 'bynum '+index+' and ('
    for turn in residues:
        turn_selection += " resid "+str(turn)
        if turn !=159 and turn !=143: #the last turns in both indexes
            turn_selection +=" or "
    turn_selection += ") and backbone"
    turns = u.select_atoms(turn_selection)
    print(turn_selection)
    dist_array = []
    for ts in u.trajectory:
        water_selection = 'resname SOL and name O* and around '+cutoff+' '+turn_selection+' '
        waters = u.select_atoms(water_selection, updating=True)
        
        dist = distances.distance_array(turns, waters, box=[172.6900, 106.8250, 45.3014, 0, 0, 0])
        distance_values = np.array(dist[0, :].flatten())
        
        for i in range(len(distance_values)):
            if distance_values[i] <= 20:
                dist_array.append(float(distance_values[i]))
            else:
                continue

    with open('water-contact-TMP.pickle', 'wb') as f:
        pickle.dump((dist_array), f)
    
    return dist_array


dist_array = calculate_water_distance(hot, str(10))
dist_array_2 = calculate_water_distance(cold, str(10))

plt.figure(figsize=(11,7))
plt.hist(dist_array, bins=60, range=(0, 15), alpha=0.2, color='red', label="'hot' turns", edgecolor='red', linewidth=0.75)
plt.hist(dist_array_2, bins=60, range=(0, 15), alpha=0.2, color='blue', label="'cold' turns", edgecolor='blue', linewidth=0.75)

plt.title("Comparing water contacts of 'facial' and 'interfacial'"+str(args.gro)+' '+str(args.index))
plt.xlabel('Distance of O SOL atom from AA turn (backbone)')
plt.ylabel('count')
plt.xlim(0, 15)
plt.ylim(0,3000)
plt.legend()
plt.show()

#print(np.shape(water_sel))
#print(np.shape(turn_sel))
#print(np.shape(dist))
