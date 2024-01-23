## Thermodynamic Analysis of Silk Fibroin-Graphite Hybrid Materials and Their Morphology
Marlo Zorman, Christian Phillips, Chenyang Shi, Shuai Zhang, James De Yoreo, Jim Pfaendtner

Silk Fibroin (SF) is a β-sheet rich protein that is responsible for the remarkable tensile strength of silk. In addition to its mechanical properties, SF is biocompatible and biodegradable, making it an attractive candidate for use in biotic/abiotic hybrid materials. A pairing of particular interest is SF with graphene-based nanomaterials (GBNs). The properties of this interface drive formation of well-ordered nanostructures and can improve electronic properties of the resulting hybrid. It was previously demonstrated that SF can form lamellar nanostructures in the presence of graphite, however the equilibrium morphology and associated driving interactions are not fully understood. In this study, we characterize these interactions between SF and SF lamellar with graphite using molecular dynamics (MD) simulations and umbrella sampling (US). We find that SF lamellar nanostructures have strong orientational and spatial preferences on graphite that are driven by the hydrophobic effect, destabilizing solvent-protein interactions, and stabilizing protein-protein and protein-graphite interactions. Finally, we show how careful consideration of these underlying interactions can be applied to rationally modify the nanostructure morphology.

### Description
Files and scripts needed to replicate all biased and unbiased simulations and analyses in (insert DOI when possible). Simulations were run with GROMACS and utilize PACKMOL to generate inputs and PLUMED to restrain coordinates. Analysis scripts require the NumPy, Pandas, Matplotlib, MDAnalysis, MDTraj, and Pymbar libraries.
#### sims
Contains folder with PACKMOL input scripts and all PDB files of individual components, as well as representative gro input structures. Also contains folder with GROMACS mdp files and representative PLUMED dat files. 
#### Files
Scripts required to reproduce all analysis performed in both the manuscript and supplemental information. Additionally includes a script used to generate free energy diagrams with MBAR.

### Dependancies
* NumPy
* Pandas
* Matplotlib
* MDAnalysis
* MDTraj
* PyMbar
