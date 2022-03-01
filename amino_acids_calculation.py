from tkinter import *


def calculate_amino_acids(codons):
    amino_acids = []
    for anticodon in codons:
        if anticodon in ["AUG"]:
            amino_acids.append("Methionine")
        elif anticodon in ["AUU", "AUC", "AUA"]:
            amino_acids.append("Isoleucine")
        elif anticodon in ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"]:
            amino_acids.append("Leucine")
        elif anticodon in ["GUU", "GUC", "GUA", "GUG"]:
            amino_acids.append("Valine")
        elif anticodon in ["UUU", "UUC"]:
            amino_acids.append("Phenylalanine")
        elif anticodon in ["UGU", "UGC"]:
            amino_acids.append("Cysteine")
        elif anticodon in ["GCU", "GCC", "GCA", "GCG"]:
            amino_acids.append("Alanine")
        elif anticodon in ["GGU", "GGC", "GGA", "GGG"]:
            amino_acids.append("Glycine")
        elif anticodon in ["CCU", "CCC", "CCA", "CCG"]:
            amino_acids.append("Proline")
        elif anticodon in ["ACU", "ACC", "ACA", "ACG"]:
            amino_acids.append("Threonine")
        elif anticodon in ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]:
            amino_acids.append("Serine")
        elif anticodon in ["UAU", "UAC"]:
            amino_acids.append("Tyrosine")
        elif anticodon in ["UGG"]:
            amino_acids.append("Tryptophan")
        elif anticodon in ["CAA", "CAG"]:
            amino_acids.append("Glutamine")
        elif anticodon in ["AAU", "AAC"]:
            amino_acids.append("Asparagine")
        elif anticodon in ["CAU", "CAC"]:
            amino_acids.append("Histidine")
        elif anticodon in ["GAA", "GAG"]:
            amino_acids.append("Glutamic Acid")
        elif anticodon in ["GAU", "GAC"]:
            amino_acids.append("Aspartic Acid")
        elif anticodon in ["AAA", "AAG"]:
            amino_acids.append("Lysine")
        elif anticodon in ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]:
            amino_acids.append("Arginine")
        elif anticodon in ["UAA", "UAG", "UGA"]:
            amino_acids.append("STOP")
        else:
            return "Invalid Input"
    amino_acids = ", ".join(amino_acids)
    return amino_acids
