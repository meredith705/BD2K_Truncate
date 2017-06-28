#MELISSA MEREDITH   Assn 2
#this shebang starts the program and sets up the code as a python program
#/usr/bin/env python
#creates the dictionary of codons and their respective tri-nucleotide sequence
codons = {  'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C', 'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C', 'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*', 'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W', 'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R', 'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', 'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R','ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S', 'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G', 'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', 'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}
#initalizes the codon_counter for the loop, starting it at zero
codon_counter = 0
#initializes the string that will hold the current codons being sequenced
current_codon = ""
#initializes the string that will list the resulting protein sequence
protein_sequence = str()
#Allowing sequence input using 'raw_input' command, so that any DNA sequence can be entered
DNA_sequence = raw_input("Name of sequence to analyze?\n")

#for loop that goes creates a variable i AND a range length equal to the length of the inputted sequence
for i in range(len(DNA_sequence)):
#making the counter add one to itself each time it goes through the loop
    codon_counter+=1
    #adding the current nucleotide to the end of the current_codon sequence
    current_codon=current_codon+DNA_sequence[i]
    #if loop that ensures that there are 3 Nucleotides to be checked against the codon dictionary
    if(codon_counter%3==0):
        #if the current_codon is in the codon dictionary and it is a stop codon, this is the first condition because there is no need to check the other conditions in case of a stop codon
        if(current_codon in codons and codons[current_codon]=="*"):
            #when the condition is met than add it to the string "protein_sequence"
            protein_sequence=protein_sequence+codons[current_codon]
            #when a stop codon is found, break the loop, since it stops the amino acid sequence
            break
        #if the 1st "if" condition is not met, than: 2nd condition: "elif" if the current_codon is IN the codon dictionary AND is not a stop codon
        elif(current_codon in codons and codons[current_codon]!="*"):
            #when the condition is met than add it to the string "protein_sequence"
            protein_sequence=protein_sequence+codons[current_codon]
            #resets the string, so that once an amino acid is coded for it resets the string, so that only 3 nucleotides are in the string at a time
            current_codon = ""
            #empties the codon conter so that it won't exceed 3, to meet the %3 if condition
            codon_counter=0
        #if the first two conditions are not met then
        else:
            #if the codon is not in the dictinaryt then print the mutation symbol in the protein sequence string
            protein_sequence=protein_sequence+"!!!"
            #in the event of a mutation break the loop
            break

#print some text and string values, from these variables, replacing the DNA_sequence "T"s with "U"s and printing it as the RNA sequence.
#print "DNA Sequence: %s\nRNA sequence: %s\nProtein Sequence: %s" % (DNA_sequence, DNA_sequence.replace('T','U'), protein_sequence)

#if loop that sets the condition if the first amino acid is an 'M' and the last protein in the string is a stop codon, its a complete sequence
if(protein_sequence[0]=='M' and protein_sequence[len(protein_sequence)-1]=="*"):
    #print the txt
    print "complete coding sequence"
#second condition that if the first amino acid is a M but the last protein in the string is not a stop codon
elif(protein_sequence[0]=='M' and protein_sequence[len(protein_sequence)-1]!="*"):
    #print the txt
    print "3'-partial coding sequence"
#second condition that if the first amino acid is a not an M but the last protein in the string is a stop codon
elif(protein_sequence[0]!='M' and protein_sequence[len(protein_sequence)-1]=="*"):
    #print the txt
    print "5'-partial coding sequence"
#third condition that if a mutation is found in the string
elif('!!!' in protein_sequence):
    #print the txt
    print "frame-shift in coding sequence"
#final condition if no of the other condtions are met
else:
    #print the txt
    print "internal partial coding sequence"
