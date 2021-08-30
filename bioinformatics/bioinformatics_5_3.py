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

seq=''
with open('sequence.nucleotide.fasta','r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        seq+=line.strip()
    #print(seq)
seq_f1 = seq
seq_f2 = seq[1:]
seq_f3 = seq[2:]

comp_dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
rev_comp_s = ''
for i in seq[::-1]:
    rev_comp_s+=comp_dic[i]
#print(rev_comp_s)
seq_r1 = rev_comp_s
seq_r2 = rev_comp_s[1:]
seq_r3 = rev_comp_s[2:]

def convert_codon_to_aa(seq):
    codon=''
    aa=''
    aa_list=[]
    codon_list=[]
    for base in seq:
        codon+=base
        if len(codon)%3 == 0:
            codon_list.append(codon)
            aa_list.append(codon_dic[codon])  
            codon=''
            if len(codon_list)%20 == 0:
                codon_str = ''.join(codon_list)
                aa_str='  '.join(aa_list)
                codon_list=[]
                aa_list=[]
                aa+=aa_str
    codon_str = ''.join(codon_list)
    aa_str = '  '.join(aa_list)
    aa+=aa_str
    return aa
#print(aa)

print(convert_codon_to_aa(seq_f1))
print(' '+convert_codon_to_aa(seq_f2))
print('  '+convert_codon_to_aa(seq_f3))
print(seq_f1)
print()
print(seq_r1[::-1])
print(convert_codon_to_aa(seq_r1))
print(' '+convert_codon_to_aa(seq_r2))
print('  '+convert_codon_to_aa(seq_r3))
