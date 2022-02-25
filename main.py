from tkinter import *
window = Tk()

def translate(input_strand):
    if "T" in input_strand:
        #  DNA to RNA
        pass
    elif "U" in input_strand:
        if mrna.get() is not "":
            # mRNA to tRNA
            pass
        else:
            # tRNA to Amino Acids
            pass


dna = StringVar()
mrna = StringVar()
trna = StringVar()
amino_acids = []

dnaFrame = Frame(window)
Label(dnaFrame, text="DNA:").pack(side=LEFT)
dna_input = Entry(dnaFrame, textvariable=dna)
dna_input.pack()

window.mainloop()
