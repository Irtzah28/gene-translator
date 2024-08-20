def translate_dna_to_protein_verbose(dna_sequence):
    protein = ""
for i in range(0, len(dna_sequence), 3):
    codon = dna_sequence[i:i+3]
    amino_acid = genetic_code.get(codon, 'X')
    protein += f"{codon} -> {amino_acid}\n"
    return protein
def main():
    dna_sequence = input("Enter a DNA sequence: ").upper()
    if not validate_dna_sequence(dna_sequence):
        print("Invalid DNA sequence. Please enter a sequence containing only A, T, C, and G.")
        return
    protein = translate_dna_to_protein_verbose(dna_sequence)
    print("The translated protein sequence is:\n")
    print(protein)