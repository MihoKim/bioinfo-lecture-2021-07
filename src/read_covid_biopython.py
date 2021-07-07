import gzip
from Bio import SeqIO

f="covid19.fasta.gz"

with gzip.open(f,'rt') as handle:
    record=SeqIO.read(handle,'fasta')

print(f"A: {record.seq.count('A')}")
print(f"C: {record.seq.count('C')}")
print(f"G: {record.seq.count('G')}")
print(f"T: {record.seq.count('T')}")

