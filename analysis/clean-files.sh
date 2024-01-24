#!/bin/bash

#for ((i=0; i<=72; i++)); do
for i in *.dat; do
#removes extra headers from restarts on ckpt node that break mbar.py reweighting 
	awk '!/#! FIELDS time d.x/' $i > tmpfile && mv tmpfile $i
    #removes extra lines from .cpt file for uniform datapoints when reweighting
    awk '!a[$1]++' $i > tmpfile && mv tmpfile $i
    #sed '$!N; /^\(.*\)\n\1$/!P; D' colvar_multi_$i > tmpfile && mv tmpfile colvar_multi_$i
done
