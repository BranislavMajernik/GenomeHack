import os

from Bio import Entrez
#Poskytnúť email
Entrez.email = "brunix@upcmail.sk"
with Entrez.einfo(db="nucleotide") as handle:
    record = Entrez.read(handle)
for field in record["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

with Entrez.esearch(db="nucleotide", term="SARS-CoV-2[ORGN]", idtype="acc", retmax="10000") as handle:
    results = Entrez.read(handle)
accs = results["IdList"]

#Stiahnuť dáta do súboru na disk pod názvom = "./data/raw/SARS-CoV-2.gbk"
filename = "./data/raw/SARS-CoV-2.gbk"
if not os.path.isfile(filename):
    with Entrez.efetch(db="nucleotide", id=accs, rettype="gb", retmode="text") as net_handle:
        with open(filename, "w") as out_handle:
            out_handle.write(net_handle.read())
    print("Saved")
