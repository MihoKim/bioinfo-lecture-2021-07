def convert_nucleotide_sequence_to_amino_acid_sequence(seq):
    codon_dic = {
        'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
        'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
        'TAT':'Y', 'TAC':'Y', 'TAA':'*', 'TAG':'*',
        'TGT':'C', 'TGC':'C', 'TGA':'*', 'TGG':'W',
        'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
        'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
        'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',
        'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
        'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
        'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
        'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    }
    a_list = []
    codon_list = []
    aa_list = []
    aa = ''
    for a in seq:
        a_list.append(a)
        if len(a_list) % 3 == 0:
            codon = ''.join(a_list)
            codon_list.append(codon)
            aa_list.append(codon_dic[codon])
            a_list = []
            if len(codon_list) % 20 == 0:
                codon_str = ''.join(codon_list)
                aa_str = '  '.join(aa_list)
                codon_list = []
                li_aa = []
                aa += aa_str
    codon_str = ''.join(codon_list)
    aa_str = '  '.join(aa_list)
    aa += aa_str
    return aa_str

def convert_sequence_to_reverse_complement_sequence(seq):
    complement_dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    reverse_complement_list = list()
    for a in seq[::-1]:
        reverse_complement_list.append(complement_dic[a])
    return ''.join(reverse_complement_list)

li_seq = []

fr = open('sequence.nucleotide.fasta', 'r')
lines = fr.readlines()
for line in lines:
    if line[0] != '>':
        li_seq.append(line.strip())
fr.close()

seq = ''.join(li_seq)

seq_f1 = seq
seq_f2 = seq[1:]
seq_f3 = seq[2:]
seq_r1 = convert_sequence_to_reverse_complement_sequence(seq)
seq_r2 = convert_sequence_to_reverse_complement_sequence(seq[:-1])
seq_r3 = convert_sequence_to_reverse_complement_sequence(seq[:-2])

print(convert_nucleotide_sequence_to_amino_acid_sequence(seq_f1))
print(' ' + convert_nucleotide_sequence_to_amino_acid_sequence(seq_f2))
print('  ' + convert_nucleotide_sequence_to_amino_acid_sequence(seq_f3))
print(seq_f1)
print()
print(seq_r1[::-1])
print(convert_nucleotide_sequence_to_amino_acid_sequence(seq_r1)[::-1])
print('  ' + convert_nucleotide_sequence_to_amino_acid_sequence(seq_r2)[::-1])
print(' ' + convert_nucleotide_sequence_to_amino_acid_sequence(seq_r3)[::-1])
