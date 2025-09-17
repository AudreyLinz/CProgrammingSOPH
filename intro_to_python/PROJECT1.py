#ACTG
def isValid(dna):
    ATCG = {'A', 'C', 'T', 'G'}
    return all(char in ATCG for char in dna)
def isRepeat(dna):
    seen = set()
    repeat = set()
    for i in range(len(dna)-9):
        subseq = dna[i:i+10]
        if subseq in seen:
            repeat.add(subseq)
        else:
            seen.add(subseq)
    return sorted(repeat)


#main
dna = input("Enter DNA: ").strip()
if len(dna) < 10 or not isValid(dna):
    print("Not valid")
    quit()
else:
    repeat = isRepeat(dna)
if repeat:
    print("Repeated dna: ")
    for seq in repeat:
        print(seq)
else:
    print("no repeats")
