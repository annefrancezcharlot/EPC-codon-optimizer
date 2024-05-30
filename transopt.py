"""Optimized translation for Pseudomonas aeruginosa, Caulobacter crescentus and
Escherichia coli """

import random
import argparse
from Bio import SeqIO

"""Table optimized for Pseudomonas aeruginosa, Caulobacter crescentus and
Escherichia coli"""

opt_table = {'A': ['GCG', 'GCC'],
 'C': ['TGC'],
 'D': ['GAC', 'GAC', 'GAC', 'GAC', 'GAT'],
 'E': ['GAG', 'GAG', 'GAA'],
 'F': ['TTC'],
 'G': ['GGC'],
 'H': ['CAC', 'CAC', 'CAC', 'CAT'],
 'I': ['ATC'],
 'K': ['AAG'],
 'L': ['CTG', 'CTG', 'CTG', 'CTG', 'CTC'],
 'M': ['ATG'],
 'N': ['AAC'],
 'P': ['CCG'],
 'Q': ['CAG'],
 'R': ['CGC'],
 'S': ['AGC', 'AGC', 'TCC','TCG'],
 'T': ['ACC'],
 'V': ['GTC'],
 'W': ['TGG'],
 'Y': ['TAC', 'TAC', 'TAC', 'TAT'],
 '*': ['TGATAA']}

def optimization(protein):
    """
    Optimizes the nucleotide sequence for a given protein sequence.
    The optimization can be adapted to the organism(s) of interest
    by modifying the opt_table dictionary.

    Parameters:
        protein (str): A string representing the amino acid sequence of the protein.

    Returns:
        str: An optimized nucleotide sequence.

    """
    ntseq = ''
    for codon in protein:
        ntseq += random.choice(opt_table[codon])
    return ntseq

def batch_optimization(filepath):
    """
    Reads protein sequences from a FASTA file, optimizes the nucleotide sequences 
    and returns a dictionary with sequence tags as keys and optimized nucleotide 
    sequences as values.

    Parameters:
        filepath : str
                   The path to the FASTA file containing protein sequences.

    Returns:
        dict: A dictionary with sequence tags as keys and optimized nucleotide sequences
    as values.
    """

    results = {}

    with open(filepath, 'r') as handle:
        records = list(SeqIO.parse(handle, "fasta"))
    for record in records:
        results[record.id] = optimization(record.seq)
    return results

def transopt(ifile, ofile):
    """Reads protein sequences from an input FASTA file, optimizes the nucleotide sequences,
    and writes the optimized sequences to an output file."""

    with open(ofile, "w") as file:
        for key, seq in batch_optimization(ifile).items():
            file.write(">"+key+"\n"+seq+"\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the input file and save the output file.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')

    args = parser.parse_args()

    transopt(args.input_file, args.output_file)
