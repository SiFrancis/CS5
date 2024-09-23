CODON_DICT = {'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu', \
'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', \
'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STP', 'UAG': 'STP', \
'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STP', 'UGG': 'Trp', \
'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', \
'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', \
'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', \
'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', \
'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met', \
'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr', \
'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', \
'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', \
'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val', \
'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala', \
'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', \
'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'}

# start codon is AUG
START_CODONS = ('AUG')
# stop codons are UAA, UAG, and UGA
STOP_CODONS = ('UAA', 'UAG', 'UGA')

def sequence(mRNA):
    for i in STOP_CODONS:
        val = mRNA[mRNA.find('AUG'):mRNA.find(i)] + i if mRNA.find(i) != -1 else None
        if val is not None:
            codonlist = []
            for j in range(0, len(val), 3):
                codonlist.append(val[j:j+3])
            return codonlist

def main():
    """
    Translate a codon sequence into proteins.
    """
    
    # mRNA = ['CCC', 'CUU', 'CAU', 'GUU', 'UAC', 'UUA', 'GUC', \
    # 'AUG', 'UGC', 'GCG', 'CGC', 'CAG', 'UUC', 'AUA', \
    # 'CCA', 'CUA', 'CGU', 'CAU', 'CUU', 'CAC', 'ACA', \
    # 'AAU', 'CCG', 'AAG', 'GCG', 'GGG', 'GUG', 'AAU', \
    # 'GAU', 'CGC', 'UUG', 'GAG', 'GUG', 'GCA', 'GAC', \
    # 'UUG', 'CAC', 'UAU', 'GGU', 'CUG', 'UCC', 'AAA', \
    # 'GAG', 'AGG', 'UGA', 'UGC', 'CUC', 'AGA', 'CGC', \
    # 'CUU', 'GAU', 'AGA', 'CGC', 'CAG', 'UUC', 'AUA']
    
    mRNA_full = "CCCCUUCAUGUUUACUUAGUCAUGUGCGCGCGCCAGUUCAUACCACUACGUCAUCUUCACACAAAUCCGAAGGCGGGGGUGAAUGAUCGCUUGGAGGUGGCAGACUUGCACUAUGGUCUGUCCAAAGAGAGGUGAUGCCUCAGACGCCUUGAUAGACGCCAGUUCAUA"
    
    mRNA_seq = sequence(mRNA_full)
    print(mRNA_seq)
    # sentinel to check whether a start
    # codon has been encountered
    start_found = False
    for codon in mRNA_seq:
        # if a start codon is encountered,
        # translate it and all subsequent
        # codons
        if codon in START_CODONS:
            start_found = True
        if start_found:
            print(CODON_DICT[codon])
        # if a stop codon is encountered,
        # exit the loop
        if codon in STOP_CODONS:
            break

if __name__ == "__main__":
    main()