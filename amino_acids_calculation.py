from tkinter import *


def calculate_amino_acids(codons):
    amino_acids = []
    for codon in codons:
        if codon in ["AUG"]:
            amino_acids.append("Methionine")
        elif codon in ["AUU", "AUC", "AUA"]:
            amino_acids.append("Isoleucine")
        elif codon in ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"]:
            amino_acids.append("Leucine")
        elif codon in ["GUU", "GUC", "GUA", "GUG"]:
            amino_acids.append("Valine")
        elif codon in ["UUU", "UUC"]:
            amino_acids.append("Phenylalanine")
        elif codon in ["UGU", "UGC"]:
            amino_acids.append("Cysteine")
        elif codon in ["GCU", "GCC", "GCA", "GCG"]:
            amino_acids.append("Alanine")
        elif codon in ["GGU", "GGC", "GGA", "GGG"]:
            amino_acids.append("Glycine")
        elif codon in ["CCU", "CCC", "CCA", "CCG"]:
            amino_acids.append("Proline")
        elif codon in ["ACU", "ACC", "ACA", "ACG"]:
            amino_acids.append("Threonine")
        elif codon in ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]:
            amino_acids.append("Serine")
        elif codon in ["UAU", "UAC"]:
            amino_acids.append("Tyrosine")
        elif codon in ["UGG"]:
            amino_acids.append("Tryptophan")
        elif codon in ["CAA", "CAG"]:
            amino_acids.append("Glutamine")
        elif codon in ["AAU", "AAC"]:
            amino_acids.append("Asparagine")
        elif codon in ["CAU", "CAC"]:
            amino_acids.append("Histidine")
        elif codon in ["GAA", "GAG"]:
            amino_acids.append("Glutamic Acid")
        elif codon in ["GAU", "GAC"]:
            amino_acids.append("Aspartic Acid")
        elif codon in ["AAA", "AAG"]:
            amino_acids.append("Lysine")
        elif codon in ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]:
            amino_acids.append("Arginine")
        elif codon in ["UAA", "UAG", "UGA"]:
            amino_acids.append("STOP")
        else:
            return "Invalid Input"
    amino_acids = ", ".join(amino_acids)
    return amino_acids
