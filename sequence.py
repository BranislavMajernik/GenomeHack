from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline

unfiltered = SeqIO.parse("./data/raw/SARS-CoV-2.gbk", "genbank")

full_length_records = []
for record in unfiltered:
    if len(record.seq) > 29000:
        full_length_records.append(record)

SeqIO.write(full_length_records, "./data/raw/SARS-CoV-2.fasta", "fasta")
#Zarovnávanie sekvencií
muscle_cline = MuscleCommandline(input="SARS-CoV-2.fasta",
                                 out="SARS-CoV-2_aligned.fasta",
                                 diags = True,
                                 maxiters = 1,
                                 log="./data/raw/align_log.txt")
muscle_cline()
