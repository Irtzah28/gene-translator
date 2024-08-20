# Gene Translation Tool

# Genetic code dictionary to map codons to amino acids
genetic_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

# Function to translate DNA to protein
def translate_dna_to_protein(dna_sequence):
    protein = ""
    # Loop through the DNA sequence in steps of 3 (codon size)
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        amino_acid = genetic_code.get(codon, 'X')  # 'X' for unknown codons
        protein += amino_acid
    return protein  # Ensure this return statement is indented correctly within the function

# Function to translate DNA to protein with verbose output
def translate_dna_to_protein_verbose(dna_sequence):
    protein = ""
    # Loop through the DNA sequence in steps of 3 (codon size)
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        amino_acid = genetic_code.get(codon, 'X')
        protein += f"{codon} -> {amino_acid}\n"
    return protein  # Ensure this return statement is indented correctly within the function

# Function to validate DNA sequence
def validate_dna_sequence(dna_sequence):
    valid_nucleotides = {'A', 'T', 'C', 'G'}
    for nucleotide in dna_sequence:
        if nucleotide not in valid_nucleotides:
            return False
    return True

# Main function
def main():
    dna_sequence = input("Enter a DNA sequence: ").upper()
    if not validate_dna_sequence(dna_sequence):
        print("Invalid DNA sequence. Please enter a sequence containing only A, T, C, and G.")
        return
    protein = translate_dna_to_protein_verbose(dna_sequence)
    print("The translated protein sequence is:\n")
    print(protein)

if __name__ == "__main__":
    main()
