
DNA = "caatgtatggagcatgaacgaccaatcactgacaaacctttaactggatagtgcactgagaaagtgccaccccggttttacgtcaag".upper()

DNA_Rep = []

for lets in DNA:
    if lets == 'G':
        DNA_Rep.append('C')
    if lets == 'C':
        DNA_Rep.append('G')
    if lets == 'A':
        DNA_Rep.append('U')
    if lets == 'T':
        DNA_Rep.append('A')

Transcription = ''.join(DNA_Rep)
Translation = []
for i in range(0, len(Transcription), 3):
    Translation.append(Transcription[i:i+3])
T_RNA = []
if 'AUG' in Translation:
    try:
        for triplet in Translation[Translation.index('AUG'):]:
            """Looks for the Start codon and begins translating the codons to AA"""
            if triplet == 'AUG':
                T_RNA.append('Met')
            if triplet in ['UUU','UUC']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Phe')
            elif triplet in ['UUA', 'UUG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Leu')
            elif triplet in ['UCU', 'UCC', 'UCA', 'UCG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Ser')
            elif triplet in ['UAA', 'UAG', 'UGA']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'STOP')
                print('You encountered a STOP Codon')
                break
            elif triplet in ['UAU', 'UAC']:
                z = Translation.index(triplet)
                T_RNA.insert(z, 'Tyr')
            elif triplet in ['UGU', 'UGC']:
                z = Translation.index(triplet)
                T_RNA.insert(z, 'Cys')
            elif triplet == 'UGG':
                z = Translation.index(triplet)
                T_RNA.insert(z, 'Trp')
            elif triplet in ['CCU', 'CCC', 'CCA', 'CCG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Pro')
            elif triplet in ['CUU', 'CUC', 'CUA', 'CUG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Leu')
            elif triplet in ['CAU', 'CAC']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'His')
            elif triplet in ['CAA', 'CAG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Gln')
            elif triplet in ['CGU', 'CGC', 'CGA', 'CGG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Arg')
            elif triplet in ['AUU', 'AUC', 'AUA']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Ile')
            elif triplet in ['ACU', 'ACC', 'ACA', 'ACG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Thr')
            elif triplet in ['AAU', 'AAC']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Asn')
            elif triplet in ['AAA', 'AAG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Lys')
            elif triplet in ['AGU', 'AGC']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Ser')
            elif triplet in ['AGA', 'AGG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Arg')
            elif triplet in ['GUU', 'GUC', 'GUA', 'GUG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Val')
            elif triplet in ['GCU', 'GCC', 'GCA', 'GCG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Ala')
            elif triplet in ['GAU', 'GAC']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Asp')
            elif triplet in ['GAA', 'GAG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Glu')
            elif triplet in ['GGU', 'GGC', 'GGA', 'GGG']:
                x = Translation.index(triplet)
                T_RNA.insert(x, 'Gly')
    except ValueError:
        print('No Start Codon')

while True:
    if 'AUG' in Translation:
        for items in Translation[:Translation.index('AUG')]:
            Translation.remove(items)
        print(Translation)
        print(T_RNA)
        break
    else:
        print('No Start Codon!')
        break


