seq=''
with open('sequence.nucleotide.fasta','r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        seq+=line.strip()
    #print(seq)

codon=''
for base in seq:
    codon += base
    if len(codon)%3 == 0:
        print(codon)
        codon=''
