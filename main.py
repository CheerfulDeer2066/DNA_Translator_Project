"""
Caiden Lineman
2/27/2022
Takes an input of DNA, mRNA, or tRNA from a user and returns corresponding DNA, mRNA, tRNA, and Amino Acid values
"""

from tkinter import *
from amino_acids_calculation import calculate_amino_acids


def translator(input_string, translation_type="DNA"):
    # NOTE!! Any string currently works as an input as long as it has either T or U, but not both at once!!
    # Make sure to check it is a valid strand of DNA/RNA before running the rest of translate()!!
    input_string = input_string.upper()
    display_text.set("")
    if translation_type == "DNA":
        # DNA to mRNA & tRNA - run only if input is DNA
        # U to - is added to the input to make the output seen as invalid - no "-" character in calculation function
        # Set DNA (base)
        dna.set(input_string)
        # Set mRNA
        mrnakey = str.maketrans("ATGCU", "UACG-")
        mrna.set(str.translate(dna.get(), mrnakey))
        # Set tRNA
        trnakey = str.maketrans("ATGCU", "AUGC-")
        trna.set(str.translate(dna.get(), trnakey))
    elif translation_type == "mRNA":
        #  mRNA to DNA & tRNA - run only if input is mRNA
        # T to - is added to the input to make the output seen as invalid - no "-" character in calculation function
        # Set mRNA (base)
        mrna.set(input_string)
        # Set DNA
        dnakey = str.maketrans("UACGT", "ATGC-")
        dna.set(str.translate(mrna.get(), dnakey))
        # Set tRNA
        trnakey = str.maketrans("UACGT", "AUGC-")
        trna.set(str.translate(mrna.get(), trnakey))
    elif translation_type == "tRNA":
        # tRNA to DNA & mRNA - run only if input is tRNA
        # T to - is added to the input to make the output seen as invalid - no "-" character in calculation function
        # Set tRNA (base)
        trna.set(input_string)
        # Set DNA
        dnakey = str.maketrans("AUGCT", "ATGC-")
        dna.set(str.translate(trna.get(), dnakey))
        # Set mRNA
        mrnakey = str.maketrans("AUGCT", "UACG-")
        mrna.set(str.translate(trna.get(), mrnakey))
    else:
        display_text.set("Invalid Translation code given.\nPlease contact this program's creator.")
    # Split the tRNA into codons
    codons = []
    for i in range(int(len(mrna.get()) / 3)):
        codons.append(mrna.get()[(3 * i):3 + (3 * i)])
    # Translate valid codons into their amino acids
    amino_acids.set(calculate_amino_acids(codons))
    if len(input_string) % 3 != 0:
        display_text.set("Some bases were not counted.\nRemember that codons are sets of 3.")
    if amino_acids.get() == "Invalid Input":
        # if string are sets of 3 and don't make acids,
        # then the characters entered aren't bases
        display_text.set("Invalid Input. Please Try Again.")
        dna.set("Invalid Input")
        mrna.set("Invalid Input")
        trna.set("Invalid Input")


if __name__ == "__main__":
    window = Tk()
    window_length, window_height = (200, 250)
    window.title("DNA Translator")
    window.minsize(window_length, window_height)

    input_var = StringVar()
    dna = StringVar()
    mrna = StringVar()
    trna = StringVar()
    amino_acids = StringVar()

    # Add DNA info
    dnaFrame = Frame(window)
    dnaFrame.pack()
    Label(dnaFrame, text="DNA:").pack()
    dna_output = Label(dnaFrame, textvariable=dna)
    dna_output.pack()

    # Add mRNA info
    mrnaFrame = Frame(window)
    mrnaFrame.pack()
    Label(mrnaFrame, text="mRNA:").pack()
    mrna_output = Label(mrnaFrame, textvariable=mrna)
    mrna_output.pack()

    # Add tRNA info
    trnaFrame = Frame(window)
    trnaFrame.pack()
    Label(trnaFrame, text="tRNA:").pack()
    trna_output = Label(trnaFrame, textvariable=trna)
    trna_output.pack()

    # Add tRNA info
    aminoacidsFrame = Frame(window)
    aminoacidsFrame.pack()
    Label(aminoacidsFrame, text="Amino Acids:").pack()
    aminoacids_output = Label(aminoacidsFrame, textvariable=amino_acids)
    aminoacids_output.pack()

    # Add terminal for errors and entry for user input
    inputFrame = Frame(window)
    display_text = StringVar()
    interface = Label(inputFrame, textvariable=display_text)
    entry = Entry(inputFrame, textvariable=input_var)
    inputFrame.pack()
    interface.pack()
    entry.pack()

    # Add buttons for the user to choose conversion type
    buttonFrame = Frame(window)
    dna_convert = Button(buttonFrame, text="DNA", command=lambda: translator(input_var.get(), "DNA"))
    mrna_convert = Button(buttonFrame, text="mRNA", command=lambda: translator(input_var.get(), "mRNA"))
    trna_convert = Button(buttonFrame, text="tRNA", command=lambda: translator(input_var.get(), "tRNA"))
    buttonFrame.pack()
    dna_convert.pack(side=LEFT)
    mrna_convert.pack(side=LEFT)
    trna_convert.pack(side=LEFT)

    window.mainloop()
