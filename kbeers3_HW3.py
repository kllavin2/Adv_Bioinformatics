# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:28:37 2019

@author: kbeers3
"""
"""
Transform the gene features of a .gff3 format to BED
#score field is 0


"""
#file to be read in
gff3 = "yeast.gff3"

#parse gff3 file
with open(gff3, 'r') as f:
    lines = f.readlines()
print(len(lines))
with open("yeast_parsed.gff3", 'w') as f:
    for line in lines:
        if line.startswith('#'):
            continue
        f.write(line)
