import re
seq = "GAGGCGTTACCCCAATCGTTCACCGTCGGATTTGCTACAGCCCCTGAA"
new = ""
for i in seq:
    if i == "A":
        new += "U"
    elif i == "C":
        new += "G"
    elif i == "T":
        new += "A"
    else:
        new += "C"
tRNA = ""
for i in new:
    if i == "A":
        tRNA += "U"
    elif i == "U":
        tRNA += "A"
    elif i == "G":
        tRNA += "C"
    else:
        tRNA += "G"
tRNA_seq = re.findall("...", tRNA)
print(tRNA_seq)
others = ",".join(tRNA_seq)
