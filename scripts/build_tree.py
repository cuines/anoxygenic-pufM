#!/usr/bin/env python3
"""
Script to build phylogenetic tree from pufM sequences.
Concatenates all .fasta files in data/pufM_sequences/ directory.
"""

import os
from Bio import SeqIO
import subprocess

def main():
    pufm_dir = "data/pufM_sequences"
    if not os.path.exists(pufm_dir):
        print(f"Directory {pufm_dir} not found.")
        return
    
    fasta_files = [f for f in os.listdir(pufm_dir) if f.endswith('.fasta')]
    if not fasta_files:
        print("No .fasta files found.")
        return
    
    concatenated = "concatenated_pufM.fasta"
    with open(concatenated, 'w') as out:
        for f in fasta_files:
            path = os.path.join(pufm_dir, f)
            for record in SeqIO.parse(path, "fasta"):
                SeqIO.write(record, out, "fasta")
    
    print(f"Concatenated {len(fasta_files)} files into {concatenated}")
    # Placeholder for alignment and tree building
    # Use MAFFT and FastTree if installed
    # subprocess.run(["mafft", "--auto", concatenated, ">", "aligned.fasta"], shell=True)
    # subprocess.run(["FastTree", "-out", "tree.newick", "aligned.fasta"], shell=True)

if __name__ == "__main__":
    main()